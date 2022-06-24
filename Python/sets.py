a = {1,2,2,3,4,5,5,6}
print(a)

b = {1,2,4,5,7,9}
b.add(8)
print(b)

c = frozenset({1,6,7,2,3})
print(c)


import random
randomset = set()
for i in range(0, 10):
    x = random.randint(0, 100)
    randomset.add(x)
print(randomset)
c = randomset.copy()
print(c)

randomlist = []
for j in range(1, 10):
    y = random.randint(1, 100)
    randomlist.append(y)
print(randomlist)