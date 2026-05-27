# 함수연습.py

# 1) 합수를 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)

# 2) 함수를 호출
retValue = setValue(5)
print(retValue)

# 값을 리턴하는 함수
def swap(a, b):
    return b, a

# 호출
retValue = swap(3, 4)
print(retValue)

# 전역변수
x = 5
def func(a):
    return a + x

# 호출
print(func(1))

def func2(a):
    # 지역변수
    x = 1
    return a + 1

#  호출
print(func2(1))

print("-------------------------------------")

# 기본값을 명시
def times(a=10, b=20):
    return a * b

# 호출
print(times())
print(times(5))
print(times(5, 6))

# 키워드 인자
def connectURI(server, port):
    strURL = "https://" + server + ":" + port
    return strURL

# 호출
print(connectURI("multi.com", "80"))
print(connectURI(port="8080", server="naver.com"))

print("---------------------------------------------")

# 디버깅 예시
def union(*ar):
    # 지역변수로 리스트 초기화
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

# 호출
print(union("HAM", "EGG"))
print(union("HAM", "EGG", "SPAM"))

print("-------------------------------------------")

# 람다 함수를 정의
g = lambda x, y : x * y
print(g(3, 4))
print(g(5, 6))
print( (lambda x:x*x)(3) )
print (dir())
print(globals())
