print ("Helo !!!")
a=10
b=20
c=30 if a<b else 40
print(c)
print(type(c))


#String formatted operators
print("%s is fruit & it is %d kg per %i Rs!!!" %('Apple', 1, 100))
s='''classes by  'xxx' for "python" is good'''
print(s)
print(type(s))

print('#'*5)
print('pune')
print('#'*5)

# list is mutable
l=[]
l.append(12)
l.append('aaa')
l.append(11.6)
l.append(True)
print(l)
l[0]=1000
print(l)

#tuple
t=(10,'aaa',44.8,False)
print(type(t))
print(t)
#print(t[1:3])
print(id(t))
# t[0]=777    #TypeError: 'tuple' object does not support item assignment bcoz it is immutabl

#t.append(33)   # AttributeError: 'tuple' object has no attribute 'append'
print(t)
print(id(t))

t1=()
t1=(10)
print(type(t1))

#set
s={10,'aaa',44.8,False,10}
print(type(s))
print(s)
#print(s[0])      #TypeError: 'set' object does not support indexing
s.add("pune")
s.remove(10)
print(s)

s1={}
print(type(s1))

s2=set()
print(type(s2))

#frozenset
fs=frozenset(s)
print(type(fs))
print(fs)
#fs.add(99)      #AttributeError: 'frozenset' object has no attribute 'add'
#fs.remove('aaa')    #AttributeError: 'frozenset' object has no attribute 'add'

fs1=frozenset({99,'kk'})
print(type(fs1))
print(fs1)
#dict
d={100:'abc',200:'xyz'}
print(type(d))
print(d)

d1={}
d1[1]='aaa'
d1[2]='zzz'
print(d1)
#range
r=range(10)
print(type(r))
print(r)
for x in r:
    print(x)

r=range(11,20)
for x in r:
    print(x)

r=range(50,20,-5)
for x in r:
    print(x)
print("*******")
r1=r[1:4]
for x in r1:
    print(x)
#r[1]=9999       #TypeError: 'range' object does not support item assignment
for x in r:
    print(x)


#bytes
l=[10,20,30]
b=bytes(l)
print(type(b))
for x in b:
    print(x)
#l=[10,20,30,256]    #ValueError: bytes must be in range(0, 256)

print(b[0])
#b[0]=44     #TypeError: 'bytes' object does not support item assignment

#bytearray
print("bytearray")
b=bytearray(l)
print(type(b))
print(b[0])
b[0]=44

#none
print("none data type")
a=None
print(id(a))
print(type(a))
def f1():
    return 10
x=f1()
print(x)

def f1():
     print("Hello")
x=f1()
print(x)

a=None
b=None
c=None
def f1():
   pass

d= f1()
print(a,b,c,d)
print(id(a),id(b),id(c),id(d))

print(("pune\tMh"))
print(("pune\nMh"))
print(("This is \' symbol"))
print(("This is \" symbol"))
print(("This is \\ symbol"))

#print & string formatting
name = 'John'
marks=85.65432
print("Name is",name,",Marks are ",marks)
print("Name is %s,Marks are %.3f"%(name,marks))
print("Name is {},Marks are {}".format(name,marks))
print("Name is {0},Marks are {1}".format(name,marks))

#input output operations
s=input("Enter ur name : ")
print(s)
i=int(input("Enter int val : "))
print(i)

#reading multiple inputs
list=[int(x) for x in input("Enter 3 nos seperated by space : ").split()]
print(list)