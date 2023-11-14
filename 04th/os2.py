import os

p = list()
assert p != None

print(f'{os.getpid()} address of p: {id(p)}')

for i in range(10):
    p.append(i)

for val in p:
    print(f'address of val: {id(val)}')
