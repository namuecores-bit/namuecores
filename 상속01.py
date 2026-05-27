class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    # 상속받고 재정의(덮어쓰기)
    def __init__(self, name, phoneNumber, subject, studentID):
        #self.name = name
        #self.phoneNumber = phoneNumber
        super().__init__(name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    def printInfo(self):
        #print(f"Info(Name:{self.name}, Phone Number: {self.phoneNumber}, " 
        #f"subject:{self.subject}, studentID: {self.studentID})")
        super().printInfo()
        print(f"Info(subject:{self.subject}, studentID: {self.studentID})")


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)
p.printInfo()
s.printInfo()



