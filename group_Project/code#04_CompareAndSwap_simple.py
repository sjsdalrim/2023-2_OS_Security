
from threading import Thread, Lock

import time
import random


    ## use array as main_memory
main_memory = [0]


def compare_and_swap(_index, _old_Value, _new_Value):
    global main_memory
    
    if (main_memory[_index] == _old_Value):
        main_memory[_index] = _new_Value
        return True
    else:
        return False


def operation():
    global main_memory

    while True:
        oldVal = main_memory[0]

        ## what you want to do in Thread
        newVal = oldVal + 1
        ##

        if (compare_and_swap(0, oldVal, newVal) == True):
            break


def worker_1(_num):
    for _ in range(_num):
        operation()


def worker_2(_num):
    for _ in range(_num):
        operation()


t1 = Thread(target=worker_1, args=(50,))
t2 = Thread(target=worker_2, args=(50,))


t1.start(), t2.start()

t1.join(), t2.join()


print('result = ' + str(main_memory[0]))
