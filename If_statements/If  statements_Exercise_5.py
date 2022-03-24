#if else and for loop
users = ['Gopi']
if len(users) == 0:
    print('\nWe need to find some users')
else:
    print(f'\nWelcome..|| {users}')
current_users = ['admin', 'gopi', 'sri', 'rohan', 'vijay', 'govardhan', 'karthi', 'subin', 'mani']
new_users = ['kaushik', 'Rohan', 'vijay', 'govardhan']
for new_user in new_users:
    if new_user in current_users:
        print(f'\n{new_user} is already taken')
#output
"""
Welcome..|| ['Gopi']

vijay is already taken

govardhan is already taken
"""
