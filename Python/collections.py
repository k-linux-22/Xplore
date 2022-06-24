'''
here we will see specialized container Datatypes available in the Collections module
'''

import collections
""" use of Counter module """
print("\n")
print("' use of Counter module '")
print("\n")

a = ["a", "b", "c", "d", "c", "e", "b"]
b = collections.Counter(a)
print(b)
print("b.most_common(1) : ", b.most_common(1))
print("\n")

x = collections.Counter(a=3, b=4, c=2)
print(x)
print("x.most_common(2) : ", x.most_common(2))
print("\n")

c = collections.Counter("abcd")
d = collections.Counter("aabbcd")
print("c: ", c)
print("d: ", d)
print("c+d: ", c+d)
print("c-d: ", c-d)
print("d-c: ", d-c)
print("\n")

""" use of Deque module """
print("' use of Deque module '")
print("\n")

dq = collections.deque([1,2,3,2,4,5,1,3,6])
print("dq: ", dq)
print("\n")

dq.append(100)
print("dq.append(100) : ", dq)

dq.appendleft(90)
print("dq.appendleft(90) : ", dq)
print("\n")

print("dq.pop : ", dq.pop())
print("dq: ", dq)
print("\n")

print("dq.popleft() : ", dq.popleft())
print("dq: ", dq)
print("\n")

print("dq.count(3) : ", dq.count(3))
print("\n")

dq.extend("2345")
print("dq.extend('2345') : ", dq)
print("\n")

dq.rotate(2)
print("dq.rotate(2) : ", dq)

dq.rotate(-2)
print("dq.rotate(-2) : ", dq)

dq.rotate(-2)
print("dq.rotate(-2) : ", dq)
