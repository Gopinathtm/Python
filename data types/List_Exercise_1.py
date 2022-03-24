#for loop and if statements in list

Dinner_guests_list = ['GOPI', 'SRI', 'KARTHI', 'SUBIN', 'MANI', 'GOVARDHAN', 'ROHAN', 'VIJAY']
for guest in Dinner_guests_list:
    print(f"{guest} welcome to the dinner")
print(f"\n{Dinner_guests_list[-3]} could not come")
del Dinner_guests_list[-3]

print("\nExtra tables available please invite more guests\nNew guests invited names are mentioned below\n")
new_guest = ["PAWAR", "RAUT", "AVIRAJ", "SRINIWAS", "VARKEES"]
for nguest in new_guest:
    print(f"Welcome {nguest} for dinner")
print()
Dinner_guests_list = Dinner_guests_list + new_guest
for table in Dinner_guests_list:
    if len(Dinner_guests_list) > 2:
        print(f"Sorry no table available Mr.{table}"
#output
              
"""
GOPI welcome to the dinner
SRI welcome to the dinner
KARTHI welcome to the dinner
SUBIN welcome to the dinner
MANI welcome to the dinner
GOVARDHAN welcome to the dinner
ROHAN welcome to the dinner
VIJAY welcome to the dinner

GOVARDHAN could not come

Extra tables available please invite more guests
New guests invited names are mentioned below

Welcome PAWAR for dinner
Welcome RAUT for dinner
Welcome AVIRAJ for dinner
Welcome SRINIWAS for dinner
Welcome VARKEES for dinner

Sorry no table available Mr.RAUT
Sorry no table available Mr.AVIRAJ
Sorry no table available Mr.SRINIWAS
Sorry no table available Mr.VARKEES  """           
