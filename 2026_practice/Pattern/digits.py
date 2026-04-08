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

print("---------------------------------------------------")
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

print("---------------------------------------------------")