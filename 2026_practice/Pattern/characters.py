print("-------------------pgm 1--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i+1):
        ch = chr(p)
        print(ch,end=" ")
    p+=1
    print()

'''
A 
B B 
C C C 
D D D D 
E E E E E
'''
print("-------------------pgm 2--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i,n):
        ch = chr(p)
        print(ch,end=" ")
    p+=1
    print()

'''
A A A A A 
B B B B 
C C C 
D D 
E 
'''

print("-------------------pgm 3--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i+1):
        ch=chr(p)
        print(ch,end=" ")
        p+=1
    print()
'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''
print("-------------------pgm 4--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(chr(p),end=" ")
        p+=1
    print()
'''
  A B C D E 
    F G H I 
      J K L 
        M N 
          O
'''

print("-------------------pgm 5--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

'''
          A 
        B C 
      D E F 
    G H I J 
  K L M N O
'''
print("-------------------pgm 6--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    p=65
    print()

'''
     A 
    A B 
   A B C 
  A B C D 
 A B C D E
 '''

print("-------------------pgm 7--------------------------")
n=5
p=65
for i in range(n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(1,i+1):
        print(chr(p),end=" ")
        p+=1
    print()

'''
    A 
   B C 
  D E F 
 G H I J 
K L M N O 
'''

print("-------------------pgm 8--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print(chr(p),end=" ")
        p+=1
    print()

'''
    A 
   B C 
  D E F 
 G H I J 
K L M N O 
'''

print("-------------------pgm 9--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(p),end=" ")
    for j in range(i):
        print(chr(p), end=" ")
    p+=1
    print()

'''
          A 
        B B B 
      C C C C C 
    D D D D D D D 
  E E E E E E E E E 
'''

print("-------------------pgm 10--------------------------")
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p),end=" ")
    p+=2
    print()

'''
A 
C C 
E E E 
G G G G 
I I I I I 
'''