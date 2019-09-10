print("casting")
#print(int('x'))


try:
    print(int('1'))
except:
    print("Conversion failed")
else:#if no-exception
    print("Conversion Successful")
finally:#always
    print('Done')