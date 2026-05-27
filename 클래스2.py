# 클래스2.py

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Skill: {self.skill}")


people = [
    Person(1, "Alice"),
    Manager(2, "Bob", "Sales Manager"),
    Employee(3, "Charlie", "Python"),
    Person(4, "Diana"),
    Manager(5, "Ethan", "HR Manager"),
    Employee(6, "Fiona", "Data Analysis"),
    Person(7, "George"),
    Manager(8, "Hannah", "IT Manager"),
    Employee(9, "Ian", "Web Development"),
    Employee(10, "Julia", "Machine Learning"),
]

for person in people:
    person.printInfo()
