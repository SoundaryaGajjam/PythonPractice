a=5
b=10

print("Before swapping ")
print(f"a = {a} and b= {b}")
tmp = a
a=b
b=tmp

print("After swapping using 3rd variable")
print(f"a = {a} and b= {b}")

a = 100
b = 200
print("****************************")
print("Before swapping ")
print(f"a = {a} and b= {b}")
# without 3rd variable
a,b = b,a

print("After swapping without 3rd variable")
print(f"a = {a} and b= {b}")

a = 55
b = 33
print("****************************")
print("Before swapping ")
print(f"a = {a} and b= {b}")

a = a+b
b = a-b
a = a-b

print("After swapping without 3rd variable - arithmatic way")
print(f"a = {a} and b= {b}")
