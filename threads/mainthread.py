from threading import *
'''
import  threading

print("Current Thread i.e. running : ",threading.current_thread())

if threading.current_thread() == threading.main_thread():
    print("main thread")
else:
    print("Some other thread")
'''
def diplayNumbers():
    i=0
    print(current_thread().getName())
    while(i<=10):
        print(i)
        i+=1
print(current_thread().getName())
t = Thread(target=diplayNumbers)
t.start()