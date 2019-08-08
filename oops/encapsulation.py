class Student:
#PrivateVariables: startswith __ & only access in method

    def __init__(self):
        self.__id=123
        self.__name='John'

    def display(self):
        print(self.__id,self.__name)
s=Student()
#print(s.id,s.name)     #without __means var is public
#print(s.__id,s.__name)  #can not access bcoz of private ...Exception: AttributeError: 'Student' object has no attribute '__id'
s.display()
#accessing private fields with obj

print(s._Student__id)   #this is called name mangling
print(s._Student__name)

'''
#using getter setter
    def setId(self,id):
        self.id=id
    def getId(self):
       return self.id

    def setName(self,nm):
       self.name=nm
    def getName(self):
       return self.name
s=Student()
s.setId(11)
s.setName("aaa")
print(s.getId())
print(s.getName())
'''