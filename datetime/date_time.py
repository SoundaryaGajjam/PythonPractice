from  datetime import *
import time
'''
import time,datetime
epochsec=time.time()
print(epochsec)
t=time.ctime(epochsec)  #tocalculate exact date & time
print(t)
dt=datetime.datetime.today()
print("Current Month : {}/{}/{}".format(dt.day,dt.month,dt.year))
print("Current Time : {}:{}:{}".format(dt.hour,dt.minute,dt.second))
'''

'''


d=date(2018,7,21)
t=time(12,45)
dt=datetime.combine(d,t)
print(dt)
'''
#knowing execution time of pgm
starttime=time.perf_counter()     #return cur time in sec
#sorting dates
ldates=[]
d1=date(2018,8,12)
d2=date(2017,8,12)
d3=date(2018,9,12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

time.sleep(3)
ldates.sort()
for d in ldates:
    print(d)

endtime=time.perf_counter()
print("Execution Time : ",endtime-starttime)