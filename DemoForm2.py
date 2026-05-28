# DemoForm.py
# DemoForm.ui (화면단) + DemoForm.py (로직단)으로 구성된  PyQt6 프로그램

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import uic

# 크롤링을 위한 선언
from bs4 import BeautifulSoup
# 웹 서버에 요청
import urllib.request
# 정규표현식
import re

# 다지안 파일을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

# 폼클래스를 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 화면단의 요소들을 초기화하는 메서드
    # 슬롯메서드 정의
    def firstClick(self):
        #self.crol()
        crol()
        self.label.setText("오늘의 유머 베스트 게시판 크롤링 완료.")
    def secondClick(self):
        self.label.setText("두 번째 버튼이 클릭되었습니다.!!!")
    def thirdClick(self):
        self.label.setText("세 번째 버튼이 클릭되었습니다.~~~")
    # def crol(self):
    #     #User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
    #     hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

    #     # 파일에 저장
    #     f = open("todayHumor.txt", "wt", encoding="utf-8")

    #     #url = "https://www.clien.net/service/board/sold"
    #     for i in range(1, 11):
    #         url = "https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=" + str(i)
    #         print(url)

    #         #data = urllib.request.urlopen(url).read()
    #         #웹브라우져 헤더 추가 
    #         req = urllib.request.Request(url, headers = hdr)
    #         data = urllib.request.urlopen(req).read()

    #         soup = BeautifulSoup(data, 'html.parser')
    #         # 필터링 작업
    #         list = soup.find_all("td", attrs={"class":"subject"})
    #         for tag in list:
    #             title = tag.find("a").text.strip()
    #             # print(title)
    #             # f.write(title + "\n")
    #             #문자열 검색(정규표현식)
    #             if re.search("한국", title):
    #                 print(title)
    #                 f.write(title + "\n")

    #     f.close()

def crol():
    #User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
    hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

    # 파일에 저장
    f = open("todayHumor.txt", "wt", encoding="utf-8")

    #url = "https://www.clien.net/service/board/sold"
    for i in range(1, 11):
        url = "https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=" + str(i)
        print(url)

        #data = urllib.request.urlopen(url).read()
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(url, headers = hdr)
        data = urllib.request.urlopen(req).read()

        soup = BeautifulSoup(data, 'html.parser')
        # 필터링 작업
        list = soup.find_all("td", attrs={"class":"subject"})
        for tag in list:
            title = tag.find("a").text.strip()
            # print(title)
            # f.write(title + "\n")
            #문자열 검색(정규표현식)
            if re.search("한국", title):
                print(title)
                f.write(title + "\n")

    f.close()


# 진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demo = DemoForm()  # DemoForm 객체 생성
    demo.show()  # 화면에 폼을 보여줌
    sys.exit(app.exec())  # 이벤트 루프 시작

