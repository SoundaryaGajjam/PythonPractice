#Duck typing
class Duck:
    def talk(self):
        print("Quack Quack")

class Human:
    def talk(self):
        print("Helloo")

def callTalk(obj):      #invoke any mtd on the obj
    obj.talk()  #dynamically it invoke the talk() based on the obj

d=Duck()
callTalk(d)

h=Human()
callTalk(h)