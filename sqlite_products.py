import sqlite3
import random
import os
from typing import List, Optional, Tuple


class ProductsDB:
    def __init__(self, db_path: str = "MyProduct.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.execute("PRAGMA foreign_keys = ON")
        self.create_table()

    def create_table(self) -> None:
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS Products (
                productID INTEGER PRIMARY KEY,
                productName TEXT NOT NULL,
                productPrice INTEGER NOT NULL
            )
            """
        )
        self.conn.commit()

    def insert_product(self, productID: int, productName: str, productPrice: int) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)",
                (productID, productName, productPrice),
            )

    def insert_products(self, rows: List[Tuple[int, str, int]]) -> None:
        with self.conn:
            self.conn.executemany(
                "INSERT OR REPLACE INTO Products (productID, productName, productPrice) VALUES (?, ?, ?)",
                rows,
            )

    def update_product(self, productID: int, productName: Optional[str] = None, productPrice: Optional[int] = None) -> int:
        fields = []
        params: List = []
        if productName is not None:
            fields.append("productName = ?")
            params.append(productName)
        if productPrice is not None:
            fields.append("productPrice = ?")
            params.append(productPrice)
        if not fields:
            return 0
        params.append(productID)
        sql = f"UPDATE Products SET {', '.join(fields)} WHERE productID = ?"
        with self.conn:
            cur = self.conn.execute(sql, tuple(params))
            return cur.rowcount

    def get_product(self, productID: int) -> Optional[Tuple[int, str, int]]:
        cur = self.conn.execute("SELECT productID, productName, productPrice FROM Products WHERE productID = ?", (productID,))
        return cur.fetchone()

    def list_products(self, limit: int = 100, offset: int = 0) -> List[Tuple[int, str, int]]:
        cur = self.conn.execute(
            "SELECT productID, productName, productPrice FROM Products ORDER BY productID LIMIT ? OFFSET ?",
            (limit, offset),
        )
        return cur.fetchall()

    def count(self) -> int:
        cur = self.conn.execute("SELECT COUNT(*) FROM Products")
        return cur.fetchone()[0]

    def generate_sample_data(self, n: int = 100_000, start_id: int = 1, batch_size: int = 2000) -> None:
        total = n
        next_id = start_id
        while total > 0:
            this_batch = min(batch_size, total)
            rows: List[Tuple[int, str, int]] = []
            end_id = next_id + this_batch
            for pid in range(next_id, end_id):
                name = f"Product {pid}"
                price = random.randint(1000, 100000)
                rows.append((pid, name, price))
            self.insert_products(rows)
            total -= this_batch
            next_id = end_id
            inserted = next_id - start_id
            print(f"Inserted {inserted} / {n}", end="\r")
        print("\nSample data generation complete.")

    def close(self) -> None:
        try:
            self.conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    db = ProductsDB()
    # If table is empty, generate 100000 sample rows.
    current = db.count()
    if current == 0:
        print("No data found. Generating 100000 sample products (this may take a while)...")
        db.generate_sample_data(100_000)
    else:
        print(f"Database already contains {current} rows. Skipping generation.")

    # Example usage
    print("Example: get product 1 ->", db.get_product(1))
    db.close()
