# Example of instance variable and class variable

class Employee:
    # Defined class variable
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        # Defined instance variables
        self.first = first
        self.last = last
        self.pay = int(pay)  # converted string to int to do calculations
        self.email = self.first + '.' + self.last + "@company.com"
        # Class variable incremented as the new object created it gets incremented
        Employee.num_of_employees += 1

    def fullname(self):
        # instance function to get fullname
        return f"{self.first} {self.last}"

    def apply_raise(self):
        # class variable used as intance variable to make changes only to this particular function
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        # Class method defined to work with class variable
        cls.raise_amount = amount


emp1 = Employee('Gopi', "TM", '50000')
emp2 = Employee('Subin', "Varkees", '60000')

# Class method argument passed
Employee.set_raise_amount(1.07)
# self passed as argument in class to understand self argument
print(Employee.fullname(emp1))
print(emp1.fullname())
print(emp1.raise_amount)
print(emp2.raise_amount)
emp1.apply_raise()
print(emp1.pay)

# changed class variable to specific method
emp1.raise_amount = 1.08
# to see all the variables of the instances
print(emp1.__dict__)

"""
Output
Gopi TM
Gopi TM
1.07
1.07
53500
{'first': 'Gopi', 'last': 'TM', 'pay': 53500, 'email': 'Gopi.TM@company.com', 'raise_amount': 1.08}
"""
