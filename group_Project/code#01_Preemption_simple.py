
from threading import Thread, Lock

import time
import random


counter = 0


def worker_1(_lock_1, _lock_2, _num):
    for _ in range(_num):

        time.sleep(random.random())

        _lock_1.acquire()

        time.sleep(random.random())
        
        if (_lock_2.locked() == True):
            _lock_1.release()
        else:
            _lock_2.acquire()
            
            ## what you want to do in worker1 Thread
            global counter
            counter += 1

            _lock_1.release()
            _lock_2.release()


def worker_2(_lock_1, _lock_2, _num):
    for _ in range(_num):

        time.sleep(random.random())

        _lock_2.acquire()
        
        time.sleep(random.random())
        
        if (_lock_1.locked() == True):
            _lock_2.release()
        else:
            _lock_1.acquire()

            ## what you want to do in worker2 Thread
            global counter
            counter += 1

            _lock_1.release()
            _lock_2.release()


lock_X = Lock()
lock_Y = Lock()

t1 = Thread(target=worker_1, args=(lock_X, lock_Y, 100))
t2 = Thread(target=worker_2, args=(lock_X, lock_Y, 100))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(counter))
