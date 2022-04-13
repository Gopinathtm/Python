# class and instance variable defined and called
class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first+'.'+self.last+"@company.com"
        Employee.num_of_employees += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee('Gopi', "TM", '50000')
emp2 = Employee('Subin', "Varkees", '60000')


emp1.raise_amount = 1.05
print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp2.num_of_employees)


"""
Output
{'first': 'Gopi', 'last': 'TM', 'pay': '50000', 'email': 'Gopi.TM@company.com', 'raise_amount': 1.05}
{'first': 'Subin', 'last': 'Varkees', 'pay': '60000', 'email': 'Subin.Varkees@company.com'}
1.05
1.04
2

"""
