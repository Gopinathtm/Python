# simple program to check try and except
try:
    print(8/0)
except ZeroDivisionError:
    print('\nAny number cannot be divided by zero')
# simple program with while loop and inputs to check try and except ValueError
print('\nGive two numbers i will add and give the answer')
print('Enter q to quit')
while True:
    first_number = input('\nEnter first number : ')
    if first_number == "q":
        break
    second_number = input('Enter second number : ')
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print(f'Please enter two integers or float')
    else:
        print(f'This is the sum of two numbers {answer}')

# simple program with while loop and inputs to check try and except FileNotFoundError
doc_name = 'gopinath.txt'
try:
    with open(doc_name) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nSorry the entered filename {doc_name} doesn't exist")

#output
"""
Any number cannot be divided by zero

Give two numbers i will add and give the answer
Enter q to quit

Enter first number : 6
Enter second number : 7
This is the sum of two numbers 13

Enter first number : 8
Enter second number : j
Please enter two integers or float

Enter first number : q

Sorry the entered filename gopinath.txt doesn't exist

"""
