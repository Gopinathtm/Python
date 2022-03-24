
#if_elif_else_by getting input from user

age = int(input("\nEnter your age : "))
if age < 2:
    print('\nThe person is baby')
elif age < 4:
    print('\nThe person is toddler')
elif age < 13:
    print('\nThe person is kid')
elif age < 20:
    print('\nThe person is a teenager')
elif age < 65:
    print('\nThe person is a adult')
else:
    print('\nThe person is older')

#output
"""
Enter your age : 3

The person is toddler
"""
