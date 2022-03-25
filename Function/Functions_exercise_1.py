#modifying a list in a function
def verify_users(users_list, verified_users):
    while users_list:
        current_user = users_list.pop()
        print(f"Verifying user {current_user.title()}")
        verified_users.append(current_user)


def show_verified_users(verified_users):
    print('\nThese are the following verified users')
    for verified_user in verified_users:
        print(verified_user.title())


name = ['gopi', 'subin', 'karthi', 'mani']
verified_name = []
verify_users(name, verified_name)
show_verified_users(verified_name)

#output
"""
Verifying user Mani
Verifying user Karthi
Verifying user Subin
Verifying user Gopi

These are the following verified users
Mani
Karthi
Subin
Gopi
"""
