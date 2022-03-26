""" simple attempt to creat a person """
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is now Eating')

    def run(self):
        print(f'{self.name} is now Running')


person1 = Human('Gopi', 25)
person2 = Human('Subin', 29)

print(f'His name is {person1.name} of age {person1.age}')
person1.eat()
print(f'His name is {person2.name} of age {person2.age}')
person2.run()

#output
"""
His name is Gopi of age 25
Gopi is now Eating
His name is Subin of age 29
Subin is now Running
"""
