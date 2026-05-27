# 파일연습.py

# 파일 객체 생성
f = open("test.txt", "wt", encoding="utf-8")  # 쓰기 모드로 파일 열기
f.write("첫번째라인\n두번째라인\n세번째라인\n")  # 파일에 문자열 쓰기
f.close()  # 파일 닫기

# 파일 읽기
f = open("test.txt", "rt", encoding="utf-8")  # 읽기 모드로 파일 열기
content = f.read()  # 파일 전체 내용 읽기
print(content)  # 읽은 내용 출력
f.close()  # 파일 닫기


