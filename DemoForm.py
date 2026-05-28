# DemoForm.py
# DemoForm.ui (화면단) + DemoForm.py (로직단)으로 구성된  PyQt6 프로그램

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt6 import uic

# 다지안 파일을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

# 폼클래스를 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 화면단의 요소들을 초기화하는 메서드
        self.label.setText("이렇게 화면에 출력!")  # 화면단의 label 요소에 텍스트 설정

# 진입점 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    demo = DemoForm()  # DemoForm 객체 생성
    demo.show()  # 화면에 폼을 보여줌
    sys.exit(app.exec())  # 이벤트 루프 시작
