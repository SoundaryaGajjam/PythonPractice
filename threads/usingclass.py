from threading import *

class MyThread:
    def displayNumbers(self):
        i = 0
        print(current_thread().getName())
        while (i <= 10):
            print(i)
            i += 1

obj=MyThread()
t1=Thread(target=obj.displayNumbers)
t1.start()

t2=Thread(target=obj.displayNumbers)
t2.start()

t3=Thread(target=obj.displayNumbers)
t3.start()