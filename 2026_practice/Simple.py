print("Hello Python")

#addition
'''
num1 = float(input("Enter first num : "))
num2 = float(input("Enter second num : "))

sum = num1+num2
print(f"sum : {num1} + {num2} = {sum}")

#Division
num3 = float(input("Enter dividend for division : "))
num4 = float(input("Enter divisior for divison : "))

if num4 == 0:
    print("Error: Division by zero is not allowed")
else:
    res = num3 / num4
    print(f"Division : {num3} / {num4} = {res}")
'''

# area of triangle
base = float(input("Enter base : "))
height = float(input("Enter height : "))
area = 0.5 * base * height
print(f"area of triangle : {area}")

import random
print(f"Random Num : {random.randint(1,100)}")

#convert kilometer to miles
km = float(input("Enter distance in km : "))
conversion_factor = 0.621371
miles = km * conversion_factor
print(f"{km} km = {miles} miles")

#convert celsius to fahernheit
celsius = float(input("Enter temp in celsius : "))
fahernheit = (celsius * 9/5) +32
print(f"{celsius} degrees celsius = {fahernheit}  degrees fahernheit")

# display calender

import  calendar
year = int(input("Enter year"))
month = int(input("Enter month"))

cal = calendar.month(year,month)
print(cal)