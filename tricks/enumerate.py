cities = ["Pune",'Mumbai',"Delhi","Goa"]
i = 0
for city in cities:
    print(i,city)
    i += 1

#using enumerate fun
print("using enumerate fun")
for i,city in enumerate(cities):
    print(i,city)