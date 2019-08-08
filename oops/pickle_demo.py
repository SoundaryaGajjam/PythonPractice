import pickle
from oops import student_pickle
'''
#serialization
f=open("student.dat","wb")
s=student_pickle.Student(123,'John',90)
pickle.dump(s,f)
print("Serialization done")
f.close()
'''
#deserialization
f=open("student.dat","rb")
obj=pickle.load(f)
obj.display()
print("deserialization done")
f.close()
