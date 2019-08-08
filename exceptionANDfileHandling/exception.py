import  logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter 2 nos : ").split()]
    logging.info("Division in progress")
    c=a/b
    print(c)
    f.write("Writing %d into file"%c)
except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Plz,enter non zero no")
    logging.error("division by 0")
else:
    print("You have entered a non zero no ")
finally:
    f.close()
    print("File closed")
print("Code after exception")