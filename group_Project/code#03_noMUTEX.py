
from threading import Thread, Lock

import time
import random


counter = 0


def worker_1(_num):

    global counter

    for _ in range(_num):

        a = counter + 0
        print('a = counter  ' + str(a) + ' ' + str(counter))
        time.sleep(0.01)
        a += 1
        print('a += 1  ' + str(a) + ' ' + str(counter))
        counter = a + 0
        print('counter = a  '  + str(a) + ' ' + str(counter))
        print(a)
        print('')


def worker_2(_num):

    global counter

    for _ in range(_num):

        b = counter + 0
        print('                    b = counter  ' + str(b) + ' ' + str(counter))
        time.sleep(0.01)
        b += 1
        print('                    b += 1  ' + str(b) + ' ' + str(counter))
        counter = b + 0
        print('                    counter = b  '  + str(b) + ' ' + str(counter))
        print('                    ' + str(b))
        print('')


def worker_3(_num):
    for _ in range(_num):

        time.sleep(random.random())

        _lock_2.acquire()
        print('worker_2 acquired lock_Y')
        
        time.sleep(random.random())
        
        if (_lock_1.locked() == True):
            _lock_2.release()
            print('worker_2 released lock_Y')
            print('                         [  FAIL ] worker_2 release Lock')
        else:
            _lock_1.acquire()
            print('worker_2 acquired lock_X')

            ## what you want to do in worker2 Thread
            global counter
            counter += 1

            _lock_1.release()
            _lock_2.release()
            print('                         [SUCCESS] worker_2 complete')



t1 = Thread(target=worker_1, args=(20,))
t2 = Thread(target=worker_2, args=(20,))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(counter))
