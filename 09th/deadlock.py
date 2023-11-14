
from threading import Thread, Lock

def worker_1(_lock_1, _lock_2):
    with _lock_1:
        print('worker_1 acquired lock_1')
        with _lock_2:
            print('worker_1 acquired lock_2')

def worker_2(_lock_1, _lock_2):
    with _lock_2:
        print('worker_2 acquired lock_2')
        with _lock_1:
            print('worker_2 acquired lock_1')

lock_1 = Lock()
lock_2 = Lock()

t1 = Thread(target=worker_1, args=(lock_1, lock_2))
t2 = Thread(target=worker_2, args=(lock_1, lock_2))

t1.start(), t2.start()

t1.join(), t2.join()
