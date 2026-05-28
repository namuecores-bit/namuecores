# web1.py

# 크롤링을 위한 선언
from bs4 import BeautifulSoup

# 연습용 웹페이지를 로딩
page = open("Chap09_test.html", "rt", encoding="utf-8").read()

# 검색용 객체 생성
soup = BeautifulSoup(page, 'html.parser')

# 전체페이지
#print(soup.prettify())

# <p>를 몽땅 검색
#print(soup.find_all("p"))

# <p class="outer-text">만 필터링
#print(soup.find_all("p", class_="outer-text"))

# attrs속성으로 검색
#print(soup.find_all("p", attrs={"class":"outer-text"}))

# id속성으로 검색
#print(soup.find("p", id="first"))

# <p>태그의 텍스트만 추출
for item in soup.find_all("p"):
    title = item.text.strip()
    # 문자열 가공
    title = title.replace("\n", "")
    print(title)

# 문자열 형식의 메서드 설명
data = "<<< 치킨 피자 햄버거 >>>"
result = data.strip("<>")  # 양쪽에서 <, > 제거
print(data)
print(result)







