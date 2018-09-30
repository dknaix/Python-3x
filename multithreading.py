"""
This is a example of multithreading in python
Dependencies: 'threading' module
Since two functions cannot run simultaniosly, we use threading for this purpose
For any querries contact dknaix.github@gmail.com
"""

import threading as t
import time


def func_1():                   #defiing function
    while 1:                    #using while loop to keep the code running
        time.sleep(1)           #using time dealy or it will flood output screen
        print("\nThread 1 running")

def func_2(): 
    while 1:
        time.sleep(1)
        print("\nThread 2 running")


t1=t.Thread(target=func_1)  #creating obj t1 and calling method 'Thread'
t1.start()                  #starting the thread i.e 't1'

t2=t.Thread(target=func_2).start()  #above code can be directly written as this
