class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public
        self._salary = salary  # Protected

    def get_salary(self):
        return self._salary

    def work(self):
        return f"{self.name} is working."

# Inherited class
class Developer(Employee):
    def work(self):
        return f"{self.name} is writing code."

# Polymorphism with inherited classes
class Manager(Employee):
    def work(self):
        return f"{self.name} is managing the team."

# Encapsulation enforced through getter
developer = Developer("Alice", 80000)
manager = Manager("Bob", 100000)

for employee in [developer, manager]:
    print(employee.work())  # Polymorphism in action
    print(f"{employee.name}'s salary: {employee.get_salary()}")
