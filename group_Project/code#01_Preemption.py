
from threading import Thread, Lock

import time
import random


counter = 0


def worker_1(_lock_1, _lock_2, _num):
    for _ in range(_num):
        while True:
            time.sleep(random.random())
    
            _lock_1.acquire()
            print('worker_1 acquired lock_X')
    
            time.sleep(random.random())
           
                ## if Y locked, release X
            if (_lock_2.locked() == True):
                _lock_1.release()
                print('worker_1 released lock_X')
                print('[FAIL] Retry worker1')
            else:
                _lock_2.acquire()
                print('worker_1 acquired lock_Y')
                
                ## what you want to do in worker1 Thread
                global counter
                counter += 1
                ##
    
                _lock_1.release()
                _lock_2.release()
                print('[SUCCESS] worker_1 complete')
                break


def worker_2(_lock_1, _lock_2, _num):
    for _ in range(_num):
        while True:
            time.sleep(random.random())
    
            _lock_2.acquire()
            print('worker_2 acquired lock_Y')
            
            time.sleep(random.random())
            
                ## if X locked, release Y
            if (_lock_1.locked() == True):
                _lock_2.release()
                print('worker_2 released lock_Y')
                print('[FAIL] Retry worker2')
            else:
                _lock_1.acquire()
                print('worker_2 acquired lock_X')
    
                ## what you want to do in worker2 Thread
                global counter
                counter += 1
                ##
    
                _lock_1.release()
                _lock_2.release()
                print('[SUCCESS] worker_2 complete')
                break


lock_X = Lock()
lock_Y = Lock()

t1 = Thread(target=worker_1, args=(lock_X, lock_Y, 50))
t2 = Thread(target=worker_2, args=(lock_X, lock_Y, 50))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(counter))
