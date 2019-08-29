class Test:
    def __init__(self):
        print("no-args constructor")
    def __init__(self,a):
        print("one-args constructor")
    def __init__(self,a,b):
        print("two-args constructor")

#t=Test()
#t=Test(10)
t=Test(10,20) # if we define multiple constructor then the last constructor will be considered


#constructor with default args
class Demo:
    def __init__(self,a=None,b=None,c=None):
        print("Constructor with 0|1|2|3 no of constructor")
d=Demo()
d1=Demo(20,30)
d2=Demo(1,1,1)

#constructor with variable no of args
class Sample:
    def __init__(self,*a):
        print("constructor with variable no of args")

s=Sample()
s1=Sample(20,30)
s2=Sample(1,1,1,1,1,1)
