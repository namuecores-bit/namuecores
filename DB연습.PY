# DB연습.py

import sqlite3

# 연결객체
conn = sqlite3.connect("c:\\work\\test.db")
# 커서객체 리턴
cur = conn.cursor()

# 테이블 생성
cur.execute("CREATE TABLE IF NOT EXISTS PhoneBook (name TEXT, PhoneNum text);")

# 입력
cur.execute("INSERT INTO PhoneBook VALUES ('홍길동', '010-1234-5678');")

# 입력 파라미터로 처리
cur.execute("INSERT INTO PhoneBook VALUES (?, ?);", ("김철수", "010-9876-5432"))

# 여러건을 입력
datalist = [("박영희", "010-5555-6666"), ("이순신", "010-1111-2222")]
cur.executemany("INSERT INTO PhoneBook VALUES (?, ?);", datalist)

# 검색
for row in cur.execute("SELECT * FROM PhoneBook;"):
    print(row)

