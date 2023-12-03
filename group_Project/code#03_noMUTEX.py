
from threading import Thread, Lock

import time
import random


counter = 0


def worker_1(_num):
    for _ in range(_num):

            ## loop until prev_a == counter(memory)
        while True:
            global counter
            a = counter
            prev_a = counter
            time.sleep(random.random())
            
            a += 1
            time.sleep(random.random())
            
            if (prev_a == counter):
                counter = a
                print('[set] ' + str(counter))
                break
            print('          loop')
            time.sleep(random.random())


def worker_2(_num):
    for _ in range(_num):

            ## loop until prev_b == counter(memory)
        while True:
            global counter
            b = counter
            prev_b = counter
            time.sleep(random.random())
            
            b += 1
            time.sleep(random.random())
            
            if (prev_b == counter):
                counter = b
                print('[set] ' + str(counter))
                break
            print('          loop')
            time.sleep(random.random())


t1 = Thread(target=worker_1, args=(50,))
t2 = Thread(target=worker_2, args=(50,))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(counter))
