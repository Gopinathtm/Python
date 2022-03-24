#While loop with input Exercise
while True:
    f_name = input('First name : ')
    if f_name == 'q':
        break
    l_name = input('Last name : ')
    if l_name == 'q':
        break
    full_name = f_name + l_name
    print(f'Welcome {full_name.title()}')
#output
"""
First name : gopi
Last name : nath
Welcome Gopinath
First name : sri
Last name : murugan
Welcome Srimurugan
First name : q
"""
