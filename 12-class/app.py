'''
class Point:
    def Move(self):
        print("move")

    def Draw(self):
        print("Draw")

point1 = Point()

point1.x = 10
point1.y = 20
print(point1.x)
point1.Draw()
'''

'''
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")

john = Person("Dav")
john.talk()
'''

class Mammal:
    def Walk(self):
        print("Walk")

class Dog(Mammal):
    def Bark(self):
        print("Bark")

class Cat(Mammal):
    pass

dog1 = Dog()
dog1.Walk()
dog1.Bark()

'''
clear
& python d:/Solutions/PythonTraining/12-class/app.py
'''