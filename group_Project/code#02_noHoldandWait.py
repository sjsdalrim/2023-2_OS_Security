
from threading import Thread, Lock

import time
import random


counter = 0


def worker_1(_lock_P, _lock_1, _lock_2, _num):
    for _ in range(_num):
        
        while True:
            if (_lock_P.acquire() == True):     ## wait Lock
                break
        
        _lock_1.acquire()
        print('worker_1 acquired lock_X')
        
        _lock_2.acquire()
        print('worker_1 acquired lock_Y')
        
        ## what you want to do in worker1 Thread
        global counter
        counter += 1
        ##

        _lock_1.release()
        _lock_2.release()
        print('[SUCCESS] worker_1 complete\n')
        _lock_P.release()
        
        time.sleep(random.random())


def worker_2(_lock_P, _lock_1, _lock_2, _num):
    for _ in range(_num):
        
        while True:
            if (_lock_P.acquire() == True):     ## wait Lock
                break
        
        _lock_2.acquire()
        print('worker_2 acquired lock_Y')
        
        _lock_1.acquire()
        print('worker_2 acquired lock_X')
        
        ## what you want to do in worker1 Thread
        global counter
        counter += 1
        ##

        _lock_2.release()
        _lock_1.release()
        print('[SUCCESS] worker_2 complete\n')
        _lock_P.release()
        
        time.sleep(random.random())


lock_Prevent = Lock()
lock_X = Lock()
lock_Y = Lock()

t1 = Thread(target=worker_1, args=(lock_Prevent, lock_X, lock_Y, 50))
t2 = Thread(target=worker_2, args=(lock_Prevent, lock_X, lock_Y, 50))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(counter))
