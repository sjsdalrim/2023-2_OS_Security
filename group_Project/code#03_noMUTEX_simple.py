
from threading import Thread, Lock

import time
import random


counter = 0


def worker_1(_num):
    for _ in range(_num):
        while True:
            global counter
            a = counter
            prev_a = counter
            
            a += 1
            
            if (prev_a == counter):
                counter = a
                break


def worker_2(_num):
    for _ in range(_num):
        while True:
            global counter
            b = counter
            prev_b = counter
            
            b += 1
            
            if (prev_b == counter):
                counter = b
                break


t1 = Thread(target=worker_1, args=(20,))
t2 = Thread(target=worker_2, args=(20,))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(counter))
