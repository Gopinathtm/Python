#for loop and if stsement
requested_toppings = ['perriperry', 'cheese', 'Chicken']
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print('\nFinished making your pizza')
else:
    print('\nSure you want plain pizza....?')

#output
"""
Adding perriperry
Adding cheese
Adding Chicken

Finished making your pizza
"""
