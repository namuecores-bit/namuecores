# 반복구문.py

# 1) whild 루프

value = 5
while value > 0:
    print(value)
    value -= 1

# 2) for in 루프
print("for ~ in ~ 루프")
for i in [1, 2, 3]:
    print(i)

# 딕셔너리
d = {"name" : "전우치", "age" : 30, "addr" : "선릉역"}
for item in d.items():
    print(item)

print("----------------------------------------")

print("---range()함수---")
print( list(range(2000, 2027)) )
print( list(range(1, 32)) )
print( list(range(1, 11, 2)) )

for i in range(5):
    print(i)

print("---리스트 컴프리헨션---")
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( [i**2 for i in lst if i > 5] )
tp = ("apple", "kiwi")
print( [len(i) for i in tp] )
d = {100 : "apple", 200 : "kiwi"}
print( [v.upper() for v in d.values()] )

print("---------------------------------------------")

print("---필터링함수 사용---")
lst = [10, 25, 30]
itemL = filter(None, lst)
for item in itemL:
    print(item)

print("-------------------")

def getBiggerThan20(i):
    return i > 20
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("---람다함수 사용---")
itemL = filter(lambda x : x > 20, lst)
for item in itemL:
    print(item)

