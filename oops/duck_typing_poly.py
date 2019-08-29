#Duck typing
class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Helloo")

def f1(obj):      #invoke any mtd on the obj
    if hasattr(obj,'talk'):
        obj.talk()  #dynamically it invoke the talk() based on the obj
    elif hasattr(obj,'bark'):
        obj.bark()

class Dog:
    def bark(self):
        print("Bow Bow")
d=Duck()
f1(d)

h=Human()
f1(h)

do=Dog()
f1(do)