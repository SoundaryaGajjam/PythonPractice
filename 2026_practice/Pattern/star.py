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

print("---------------------------------------------------")
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
