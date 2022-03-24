# Dictionary with loop
subin_info = {'f_name': 'subin',
              'l_name': 'varkees',
              'age': '29',
              'state': 'tamilnadu',
              'work': 'bfl', }
print(subin_info['f_name'])
print(subin_info['l_name'])
print(subin_info['age'])
print(subin_info['state'])
favourite_number = {'gopi': 3,
                    'subin': 7,
                    'sri': 1,
                    'mani': 5,
                    'karthi': 10}
number = favourite_number['subin']
print(f"\nSubin favourite number is {number}")
print()
favourite_number['vijay'] = 8
favourite_number['ajith'] = 11
print(f'\n{favourite_number}')
print()
for name, number in favourite_number.items():
    print(f"{name} favourite number is {number}")
glossary = {'python': 'User friendly lanuage',
            'OOPS': 'Object oriented programming language',
            'if and for': 'loop',
            'variable': 'A bucket to store information', }
print()
for concepts, meaning in glossary.items():
    print(f"{concepts} : {meaning}")
#output
"""
{'gopi': 3, 'subin': 7, 'sri': 1, 'mani': 5, 'karthi': 10, 'vijay': 8, 'ajith': 11}

gopi favourite number is 3
subin favourite number is 7
sri favourite number is 1
mani favourite number is 5
karthi favourite number is 10
vijay favourite number is 8
ajith favourite number is 11

python : User friendly lanuage
OOPS : Object oriented programming language
if and for : loop
variable : A bucket to store information
"""
