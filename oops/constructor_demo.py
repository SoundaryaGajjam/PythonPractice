class Products:
#default constructor
    def __init__(self):
        self.name='iPhone'
        self.discription='awsesome'
        self.price=50000
#instance method
    def display(self):
        print(self.name, self.discription, self.price)

pObj=Products()
pObj1=pObj      #False
pObj1=pObj      #True
#print(pObj.name,pObj.discription,pObj.price)
#print(pObj1.name,pObj1.discription,pObj1.price)
pObj.display()
pObj1.display()
print(pObj is pObj1)

class Course:
#Parameterized Constructor
    def __init__(self, name, ratings):
        self.name=name
        self.ratings=ratings

#instacnce method
    def average(self):
        noOfRatings=len(self.ratings)
        avg=sum(self.ratings)/noOfRatings
        print("Avg rating for ", self.name ," is", avg)

cObj=Course('Java', [1,2,3,4,5])
print(cObj.name,cObj.ratings)
cObj.average()
cObj1=Course('Python', [3,4,5])
print(cObj1.name,cObj1.ratings)
cObj1.average()

