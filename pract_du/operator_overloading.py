# + overloading
class Book:
    def __init__(self,pages):
        self.pages=pages

    def __add__(self, other):   #magic mtd for + operator
        return self.pages+other.pages

b1=Book(100)
b2=Book(200)
print("Total no. of pages : ",b1+b2)

# * overloading
class Employee:
    def __init__(self,name,sal):
        self.name=name
        self.salary=sal

    def __mul__(self, other):
        return self.salary*other.days

class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days

    #def __mul__(self, other):
        #   return self.days*other.salary

e=Employee("XYZ",500)
t=Timesheet("XYZ",25)
print("This month sal : ",e*t)
#print("This month sal : ",t*e)