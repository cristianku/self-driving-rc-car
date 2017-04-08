import threading
import time

def function1():
  for i in range(1,10):
    print "function 1 - " , i
    time.sleep(.3)

def function2():
    for x in range(1,10):
        print "function 2 - " , x
        time.sleep(.3)

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)

t1.start()
#t1.join()

t2.start()
#t2.join()