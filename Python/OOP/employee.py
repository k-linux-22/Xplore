class Employee:
    count = 0 # a variable to keep count of employees

    def __init__(self, name):
        self.name = name
        Employee.count += 1 # increase count when an employee is added
    
    def remove(self):
        print(f"\n{self.name} has been removed") # employee is removed
        Employee.count -= 1
    
    def greeting(self):
        print(f"\n\nHi, my name is {self.name}.") # greeting by an employee
    
    @classmethod
    def get_count(cls):
        print(f"\nNumber of Employees present : {cls.count}")

employee1 = Employee("John")
employee1.greeting()
Employee.get_count()

employee2 = Employee("Mark")
employee2.greeting()
Employee.get_count()

employee3 = Employee("Mary")
employee3.greeting()
Employee.get_count()

print("\n\nEmployee creation complete. Removing process begins.")

employee1.remove()
employee2.remove()

Employee.get_count()