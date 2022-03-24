#Example program with for loop in list
friends = ['GOPI', 'SRI','ROHAN', 'VIJAY','GOVARDHAN', 'KARTHI', 'SUBIN', 'MANI']
print("\nThese are all employees at Bharat forge")
for friend in friends:
    print(friend)
bfl = friends[:]
print("\nThese are Gopi's best friends")
for bestfriend in friends[:4]:
    print(bestfriend)
print("\nSrinivas roommates")
print(bfl[:2])
print("\nSubin roommates")
print(friends[-3:])
friends.append("RAMESH")
print("\nOne GH guy added to subinroom")
print(friends[-4:])
