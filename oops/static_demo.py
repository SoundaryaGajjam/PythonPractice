class Student:
#static field
    major = "CSE"
    noOfObj = 0

    def __init__(self,roll,nm):
        self.rollno=roll
        self.name=nm
        Student.noOfObj += 1

    @staticmethod
    def displayCount():
        print("Total no of obj : ", Student.noOfObj)


s1=Student(1,"bill")
s2=Student(2,"john")
print(s1.major)
print(Student.major)
print(s1.name)
print(s2.name)
Student.displayCount()