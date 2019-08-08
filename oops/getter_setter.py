class Programmer:
#getter-setter
#accessor & mutator methods

    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary=sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self,tech):
        self.technologies=tech

    def getTechnologies(self):
        return self.technologies

pObj=Programmer()
pObj.setName('Radha')
pObj.setSalary(15000)
pObj.setTechnologies(["Java", "C", "C++"])

print(pObj.getName(), pObj.getSalary(), pObj.getTechnologies())