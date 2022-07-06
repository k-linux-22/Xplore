class Person:
    pass # do nothing
p = Person()
print(p)

# the self keyword
class Sample:
    def message(self):
        print("Hi")

sample = Sample()
sample.message()

# init method
class Person:
    def __init__(self, name):
        print("initialized")
        self.name = name

    def message(self):
        print(f"Hi, I am {self.name}.")

p = Person("Mark")
p.message()
