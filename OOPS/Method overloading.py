# Tried method over loading in python

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a=None, b=None, c=None):
        s = 0

        if a is not None and b is not None and c is not None:
            s = a+b+c
        elif a is not None and b is not None:
            s = a + b
        else:
            s = a
        return s


gopi = Student(90, 95)
print(gopi.sum(34, 34, 67))

"""
Output

135

"""
