import os,sys
'''
f=open("myfile_demo.txt","w")
print("Enter text(Type $ when writing is done)")
s=''
while s !='$':
    s=input()
    f.write(s+'\n')
f.close()
'''
if os.path.isfile("myfile_demo.txt"):
    f=open("myfile_demo.txt","r")
    s=f.read()
    print(s)
    f.close()
else:
    print("file not exist")
    sys.exit(0)
    
