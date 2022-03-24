#if statement and for loop in two lists
availabe_toppings = ['mushroom', 'olives', 'green peppers', 'peppermint', 'pineapple', 'extra cheese']
requested_toppings = ['mushroom', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in availabe_toppings:
        print(f'Adding {requested_topping}')
    else:
        print('Sorry today french fries are not available')
print('\nYour pizza is ready')
#output
"""
Sorry today french fries are not available
Adding extra cheese

Your pizza is ready
"""
