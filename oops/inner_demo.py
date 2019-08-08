#outer cls
class Car:
    def __init__(self, make, yr):
        self.make=make
        self.year=yr
#inner cls
    class Engine:
        def __init__(self,no):
            self.number=no

        def start(self):
            print("Engine started")

c = Car("BMW", 2017)
e=c.Engine(123)
e.start()