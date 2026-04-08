print("---------------------pgm 1------------------------------")
#s = int(input("Enter a no"))
s=5
for i in range(1,s+1):
    print("* "*i)
    i+=1

'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

print("---------------------pgm 2------------------------------")
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for k in range(i+1):
        print("*",end=" ")
    print()

'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
 '''

print("---------------------pgm 3------------------------------")
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

'''
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
'''

print("---------------------pgm 4------------------------------")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()

'''
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
'''

print("---------------------pgm 5------------------------------")
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
 '''

print("---------------------pgm 6------------------------------")
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

'''
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
'''
print("---------------------pgm 7------------------------------")
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

'''
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 
'''
print("---------------------pgm 8------------------------------")
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()

'''
*                 * 
* *             * * 
* * *         * * * 
* * * *     * * * * 
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * * 
* *             * * 
*                 * 

'''