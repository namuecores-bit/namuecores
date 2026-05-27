# 전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg

    def set2(self, msg):
        global strName 
        strName = msg

    def print(self):
        print(strName)

    def print2(self):
        print(self.strName)

d = DemoString()
d.set("First Message")
d.print()
d.print2()

d.set2("Change Message")
d.print()
