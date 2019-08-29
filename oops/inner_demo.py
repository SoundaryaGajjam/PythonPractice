#outer cls
class Car:
    def __init__(self, make, yr):
        self.make=make
        self.year=yr
    def display(self):
        print(self.make,self.year)
#inner cls
    class Engine:
        def __init__(self,no):
            self.number=no

        def start(self):
            print("Engine started")

        def display(self):
            print(self.number)



c = Car("BMW", 2017)
e=c.Engine(123)
e.start()
c.display()
e.display()

c1=Car("Audi",2019).Engine(999)
c1.start()
#c1.display()