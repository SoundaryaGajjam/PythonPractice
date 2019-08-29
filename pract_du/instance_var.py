class Test:
    def __init__(self):
        self.empNo=10   #instance var inside constructor by using self var
        self.empName='abc'

    def m1(self):
        self.a=100      #instance var inside instance mtd by using self var
        print(self.a)   #accessing instance var within cls by using self var

    def m2(self):
        del self.empName    #deleting instance var within cls using self var
e=Test()
e.m1()
e.b=200     #instance var outside of the cls by using obj ref var
print(e.empNo,e.empName)    #accessing instance var outside the cls by using obj ref
#print(Test.__dict__)
print(e.__dict__)
e.m2()
print(e.__dict__)
del e.a     #deleting instance var outside the cls using obj ref
print(e.__dict__)