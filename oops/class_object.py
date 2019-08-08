class Employee:
    'Common base cls for all emps'
    empCnt=0

    def __init__(self, nm, sal):
        self.name=nm
        self.salary=sal
        Employee.empCnt+=1

    def displayCount(self):
        print("Total emp count : %d" % Employee.empCnt)

    def displayEmp(self):
        print("Name : ", self.name, " Salary : ", self.salary)

e1 = Employee('AAA', 22000)
e1.displayCount()
e1.displayEmp()

e2 = Employee('BBB', 52000)
e2.displayCount()
e2.displayEmp()

#Built-in classes
print("Employee.__doc__ : ", Employee.__doc__)
print("Employee.__name__ : ", Employee.__name__)
print("Employee.__module__ : ", Employee.__module__)
print("Employee.__bases__ : ", Employee.__bases__)
print("Employee.__dict__ : ", Employee.__dict__)
