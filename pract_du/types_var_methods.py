class Student:
    clgname="XYZ" #static var
    def __init__(self,x,y):
        self.name=x     #instance var
        self.rollno=y    #instance var

    def display(self):  #instance mtd
        print("Hello Myself is : ",self.name)
        print("My roll no is : ",self.rollno)

    @classmethod #decorator
    def getCollegeName(cls):    #class mtd
        print("College name : ",cls.clgname)

    @staticmethod
    def findAverage(x,y):       #static mtd
        print("Avg : ",(x+y)/2)

s1=Student('ABC',100)
s1.display()
s1.getCollegeName()
s1.findAverage(10,20)   #accessing the static mtd with @staticmethod
Student.findAverage(10,20) #accessing the static mtd without @staticmethod