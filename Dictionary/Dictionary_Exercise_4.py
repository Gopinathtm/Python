#While loop with flag Exercise
responses = {}
polling_active = True
while polling_active:
    name = input('Enter your name : ')
    mountain = input('Which mountain you would like to climb : ')
    responses[name] = mountain
    repeat = input('would you like to add someone yes/no')
    if repeat == 'no':
        polling_active = False
print('\n Poll results')
for name, mountain in responses.items():
    print(f"{name} would like to climb {mountain}")
#output
"""
Enter your name : gopi
Which mountain you would like to climb : everest
would you like to add someone yes/noyes
Enter your name : subin
Which mountain you would like to climb : abu
would you like to add someone yes/nono

 Poll results
gopi would like to climb everest
subin would like to climb abu
"""
