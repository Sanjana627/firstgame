class Person:
    company="India"
    def __init__(self):
        print("Initializing Person...\n")
    def takeBreathe(self):
        print("i am breathing")

class Employee(Person):
    company="Fieverr"
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"the Salary is {self.salary}")

    def takeBreathe(self):
        print("i m an employee and luckily i m breathing")

class Programmer(Employee):
    company="honda"

    def __init__(self):
        # super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"no salary to programmer")

    def takeBreathe(self):
        print("i m programmer and breathing")

p=Programmer()
p.takeBreathe()
print(p.company)




