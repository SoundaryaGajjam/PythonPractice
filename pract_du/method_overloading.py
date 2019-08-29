class Test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('Sum of 3 nos : ',a+b+c)
        elif a!=None and b!=None:
            print("Sum of 2 nos : ",a+b)
        else:
            print("pls provide 2 or 3 nos")
t=Test()
t.sum(10,20,30)
t.sum(10,20)
t.sum(10)

# pgm with var no of args
class Demo:
    def sum(self,*a):
        total=0
        for x in a:
            total+=x
        print("Sum : ",total)
d=Demo()
d.sum(10,20,30,40)
d.sum(20)
d.sum()