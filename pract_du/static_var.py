class Test:
    a=10    #static var within cls but outside of any mtd

    def __init__(self):
        Test.b=20   #static var inside constructor by using cls nm
        print(self.a)   #accessing static var inside constructor by using self
        print(Test.a)   #accessing static var inside constructor by using cls name
    def m1(self):
        Test.c=30   #static var inside instance method by using cls nm
        print(self.c)   #accessing static var inside instance mtd by using self
        print(Test.c)   #accessing static var inside instance mtd by using cls nm
    @classmethod
    def m2(cls):
        cls.d1=40   #static var inside cls mtd by using cls var
        Test.d2=400     #static var inside cls mtd by using cls nm
        print(cls.d2)   #accessing static var inside cls mtd by using cls var
        print(Test.d1)  #accessing static var inside cls mtd by using cls name
    @staticmethod
    def m3():       #static var inside static mtd by using cls nm
        Test.e=50
        print(Test.e)   #accessing static var inside static mtd by using cls name

#print(Test.__dict__)
t=Test()
t.m1()
Test.m2()
Test.m3()
Test.f=60   # static var outside the cls by using cls name
print(Test.f)   #accessing static var outside the cls by using cls name
print(t.f)      #accessing static var outside the cls by using obj ref

