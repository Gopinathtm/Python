import datetime
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

    @classmethod
    def from_string(cls, emp_str):
        # defining class method to pass strings as arguments for instances
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_work_day(day):
      # defined static method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Gopi', "TM", '50000')
emp2 = Employee('Subin', "Varkees", '60000')

emp_str_1 = 'mani-kandan-40000'
emp_str_2 = 'karthi-keyan-60000'
emp_str_3 = 'ramesh-g-80000'

new_emp1 = Employee.from_string(emp_str_1)
new_emp2 = Employee.from_string(emp_str_2)
new_emp3 = Employee.from_string(emp_str_3)

print(new_emp1.fullname())
print(new_emp2.fullname())
print(new_emp3.fullname())

# called static method
my_date = datetime.date(2022, 4, 17)
print(Employee.is_work_day(my_date))

"""
output

mani kandan
karthi keyan
ramesh g
False

"""
