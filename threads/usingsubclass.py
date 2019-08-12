from threading import Thread
#extending the thread class
class MyThread(Thread):
    def run(self) :
        i = 0
        while (i <= 10):
            print(i)
            i += 1

t=MyThread()
t.start()