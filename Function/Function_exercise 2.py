#functions with arbitary arguments

def make_pizza(size, *toppings):
    print(f'\nMaking {size} inch pizza with following toppings')
    for topping in toppings:
        print(f'-\t{topping}')


#functions with arbitary keyword arguments
make_pizza(16, 'spicytopping')
make_pizza(22, 'chicken', 'jam', 'peproni', 'extra cheese')


def build_profile(f_name, l_name, **user_info):
    user_info['firstname'] = f_name
    user_info['lastname'] = l_name
    return user_info


user_info = build_profile("albert", "einstein",
                          location='prince  ton',
                          field='physics')
print(user_info)


#output
"""
Making 16 inch pizza with following toppings
-	spicytopping

Making 22 inch pizza with following toppings
-	chicken
-	jam
-	peproni
-	extra cheese
{'location': 'prince  ton', 'field': 'physics', 'firstname': 'albert', 'lastname': 'einstein'}
"""
