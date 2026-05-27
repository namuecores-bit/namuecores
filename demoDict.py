# demoDict.py

# 사전식구조
colors =  {"apple":"red", "banana":"yellow"}
print(len(colors))

# 입력
colors["cherry"] = "red"

# 수정
colors["apple"] = "blue"
print(colors)

# 삭제
del colors["apple"]

# 반복문
for item in colors.items():
    print(item)

# 검색
print(colors["banana"])

print("----------------------------------")

