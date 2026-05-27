# 내장라이브러리.py

import random

print(random.random())  # 0.0 이상 1.0 미만의 난수 생성
print(random.random())  # 0.0 이상 1.0 미만의 난수 생성

# 구간을 지정
print(random.uniform(2.0, 5.0))  # 2.0 이상 5.0 미만의 난수 생성
print(random.uniform(2.0, 5.0))  # 2.0 이상 5.0 미만의 난수 생성

# 리스트에서 랜덤하게 선택
items = ['apple', 'banana', 'cherry', "date", "elderberry"]
print(random.choice(items))  # 리스트에서 랜덤하게 하나 선택

# 루프를 돌면서 0에서 19까지의 숫자 중에서 랜덤하게 10개를 선택
print([random.randrange(20) for i in range(10)])  # 0에서 19까지의 숫자 중에서 랜덤하게 10개 선택
print([random.randrange(20) for i in range(10)])  # 0에서 19까지의 숫자 중에서 랜덤하게 10개 선택

# 로또번호
print(random.sample(range(1, 46), 5))  # 1에서 45까지의 숫자 중에서 랜덤하게 5개 선택

# 파일명 다루기
import os.path
filename = "c:\\python313\\python.exe"

# raw string notation
filename = r"c:\python313\python.exe"

print(os.path.basename(filename))  # 파일명 추출
print(os.path.abspath("python.exe"))  # 절대 경로 추출

if os.path.exists(filename):
    print("파일이 크기 : {0}".format(os.path.getsize(filename)))  # 파일 크기 추출
else:
    print("파일이 존재하지 않습니다.")

# 운영체제의 정보
import os

print("운영체제 이름:", os.name)  # 운영체제 이름 출력
print("운영체제 환경 변수:", os.environ)  # 운영체제 환경 변수 출력
#os.system("notepad.exe")  # 메모장 실행

# 특정 폴더의 파일리스트
import glob
#print(glob.glob("c:\\work\\*.*"))  # c:\work 폴더의 모든 파일 리스트 출력
print(glob.glob(r"c:\work\*.*"))  # c:\work 폴더의 모든 파일 리스트 출력
#print(glob.glob("c:/work/*.*"))  # c:\work 폴더의 모든 파일 리스트 출력

for item in glob.glob(r"c:\work\*.*"):
    print(item)





