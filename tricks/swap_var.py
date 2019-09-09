#x = 10
#y = 20
x,y = 10,20
print('swaping  using 3rd var')
print("Before : x=%d y=%d" %(x,y))
#swap 2 var using 3rd var
tmp = x
x = y
y = tmp
print("After : x=%d y=%d" %(x,y))

#swaping without using 3rd var
x,y = 30,40
print("swaping without using 3rd var")
print("Before : x=%d y=%d" %(x,y))
x,y = y,x
print("After : x=%d y=%d" %(x,y))

