""" simple attempt to creat a person """
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # Default attribute
        self.sex = 'Male'

    def eat(self):
        print(f'{self.name} is now Eating')

    def update_age(self, age):
        self.age = age

    def increase_age(self, age):
        self.age += age

    def run(self):
        print(f'{self.name} is now Running')


person1 = Human('Gopi', 25)
person2 = Human('Subin', 29)
# modifying the attributes directly
person1.age = '28'
# modifying the attributes by passing a method
person2.update_age(32)
# incrementing attributes value through a method
person2.increase_age(2)

print(f'\nHis name is {person1.name} of age {person1.age} and {person1.sex}')
person1.eat()

print(f'\nHis name is {person2.name} of age {person2.age}')
person2.run()
#output
"""
His name is Gopi of age 28 and Male
Gopi is now Eating

His name is Subin of age 34
Subin is now Running
"""
