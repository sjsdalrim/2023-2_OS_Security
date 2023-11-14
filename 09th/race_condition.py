
from multiprocessing import Process, Value

def increment(_val: Value):
    for _ in range(100000):
        _val.value += 1


v = Value('i', 0)
p1 = Process(target=increment, args=(v, ))
p2 = Process(target=increment, args=(v, ))

p1.start(), p2.start()
p1.join(), p2.join()
print(v.value)
