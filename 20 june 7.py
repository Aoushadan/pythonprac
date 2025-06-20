class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.student_name}")

# Example usage:
student1 = Student(101, "Alice")
student1.display()


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
rect = Rectangle(5, 3)
print("Area of Rectangle:", rect.area())


class Employee:
    def __init__(self, emp_id, name, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary  # base salary
        self.department = department

    def calculate_overtime_pay(self, hours, rate_per_hour):
        return hours * rate_per_hour

# Example usage:
emp = Employee(2001, "John Doe", 50000, "Engineering")
overtime = emp.calculate_overtime_pay(10, 50)
print(f"Overtime Pay for {emp.name}: ${overtime}")


def sum_and_product(numbers):
    total = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return total, product

# Example usage:
nums = [2, 3, 4]
s, p = sum_and_product(nums)
print("Sum:", s)
print("Product:", p)
