import sqlite3
import os
from typing import List, Tuple


DB_FILE = os.path.join(os.path.dirname(__file__), 'bycle.db')


def get_conn():
    return sqlite3.connect(DB_FILE)


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Bycle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price INTEGER NOT NULL,
        qty INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


def count_rows() -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM Bycle')
    n = cur.fetchone()[0]
    conn.close()
    return n


def insert_many(rows: List[Tuple[str, int, int]]):
    conn = get_conn()
    cur = conn.cursor()
    cur.executemany('INSERT INTO Bycle (name, price, qty) VALUES (?, ?, ?)', rows)
    conn.commit()
    conn.close()


def seed_default(n: int = 100):
    init_db()
    existing = count_rows()
    if existing >= n:
        return
    to_add = n - existing
    rows = []
    # generate deterministic but varied names
    makes = ['Aurora', 'Nimbus', 'Vector', 'Falcon', 'Harbor', 'Atlas', 'Comet', 'Orion', 'Zenith', 'Pioneer']
    types = ['Road', 'Hybrid', 'Mountain', 'City', 'Folding']
    for i in range(existing + 1, existing + to_add + 1):
        name = f"{makes[i % len(makes)]} {types[i % len(types)]} {i}"
        price = 100000 + (i * 137) % 900000  # variety
        qty = (i * 7) % 20 + 1
        rows.append((name, price, qty))
    insert_many(rows)


def insert_item(name: str, price: int, qty: int) -> int:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('INSERT INTO Bycle (name, price, qty) VALUES (?, ?, ?)', (name, price, qty))
    conn.commit()
    rowid = cur.lastrowid
    conn.close()
    return rowid


def update_item(item_id: int, name: str, price: int, qty: int) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('UPDATE Bycle SET name=?, price=?, qty=? WHERE id=?', (name, price, qty, item_id))
    conn.commit()
    conn.close()


def delete_item(item_id: int) -> None:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('DELETE FROM Bycle WHERE id=?', (item_id,))
    conn.commit()
    conn.close()


def search_items(keyword: str = '') -> List[Tuple[int, str, int, int]]:
    conn = get_conn()
    cur = conn.cursor()
    if keyword:
        q = f"%{keyword}%"
        cur.execute('SELECT id, name, price, qty FROM Bycle WHERE name LIKE ? ORDER BY id', (q,))
    else:
        cur.execute('SELECT id, name, price, qty FROM Bycle ORDER BY id')
    rows = cur.fetchall()
    conn.close()
    return rows


if __name__ == '__main__':
    # when run directly, initialize and seed
    seed_default(100)
    print('Initialized and seeded bycle.db')
