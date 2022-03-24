#Conditional tests
lunch = 'Rice'
print('\n')
print("Is lunch == 'rice'..? i predict its true")
print(lunch.lower() == "rice")
print("Is  lunch == 'chapati' i predict its false")
print(lunch == "chapati")
print('\n')
things = ['pen', 'pencil', 'book', 'a4 sheet', 'pad']
print('pen' in things)
print('pad' not in things)
if 'pencil' in things:
    print('\nPencil is in things')

#output
"""
Is lunch == 'rice'..? i predict its true
True
Is  lunch == 'chapati' i predict its false
False


True
False

Pencil is in things
"""
