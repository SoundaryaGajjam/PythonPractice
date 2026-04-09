print("-------------------pgm 1--------------------------")
s=5
for i in range(1,s+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    i+=1

'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
print("-------------------pgm 2--------------------------")
n=5
num=1
for i in range(0,n):
    for j in range(0,i+1):
        print(num, end=" ")
        num+=1
    print()

'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''

print("-------------------pgm 3--------------------------")
n=5
for i in range(n):
    p=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print(p,end=" ")
        p+=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()
'''
          1 
        1 2 3 
      1 2 3 4 5 
    1 2 3 4 5 6 7 
  1 2 3 4 5 6 7 8 9 
'''

print("-------------------pgm 4--------------------------")
n=5
p=5
for i in range(n):
    k=p
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(k,end=" ")
        k-=1
    p-=1
    print()
'''
  5 4 3 2 1 
    4 3 2 1 
      3 2 1 
        2 1 
          1 
'''

print("-------------------pgm 4--------------------------")
n=5
p=1
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p+=1
    print()

'''
          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 
'''

print("-------------------pgm 5--------------------------")
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i+1,n):
        print(p,end=" ")
    p+=1
    print()

'''
          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 
    6 6 6 6 6 6 6 
      7 7 7 7 7 
        8 8 8 
          9 
'''

print("-------------------pgm 6--------------------------")
n=5
p=6
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i+1,n):
        print(p,end=" ")
    p+=1
    print()

'''
  6 6 6 6 6 6 6 6 6 
    7 7 7 7 7 7 7 
      8 8 8 8 8 
        9 9 9 
          10 
'''

print("-------------------pgm 7--------------------------")
n=5
p=1
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(p,end=" ")
    for j in range(i):
        print(p,end=" ")
    p+=1
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(p,end=" ")
    for j in range(i+1,n):
        print(p,end=" ")
    p-=1
    print()

'''
          1 
        2 2 2 
      3 3 3 3 3 
    4 4 4 4 4 4 4 
  5 5 5 5 5 5 5 5 5 
    4 4 4 4 4 4 4 
      3 3 3 3 3 
        2 2 2 
          1 
'''