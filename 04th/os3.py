from multiprocessing import Process, Value


def add_one(_val: Value):
    for _ in range(100000)
        _val.value += 1


v = Value('i', 0, lock = True)
p1 = Process(target=add_one, args=(v,))
p2 = Process(target=add_one, args=(v,))


p1.start()
p2.start()

p1.join()
p2.join()

print(v.value)
