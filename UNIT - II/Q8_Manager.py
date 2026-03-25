# Base class 1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Base class 2
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Salary:", self.salary)


# Derived class (Multiple Inheritance)
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        self.department = department

    def display_manager(self):
        self.display_person()
        self.display_employee()
        print("Department:", self.department)


# Object creation
m1 = Manager("ABC", 21 , 999, 100000, "Marketing")
m1.display_manager()