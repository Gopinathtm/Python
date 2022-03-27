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
file_name = 'gopinath.txt'
try:
    with open(file_name) as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nSorry the entered filename {file_name} doesn't exist")
# simple program with while loop and inputs to check try and except FileNotFoundError,
# if succeeds print number of words in the file
bookname = 'Alice_in_Wonderland.txt'
try:
    with open(bookname, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"\nSorry the entered filename {bookname} doesn't exist")
else:
    words = contents.split()
    num_words = len(words)
    print(f"\n\nThe book {bookname} contains {num_words} words in it")

#output
"""
Any number cannot be divided by zero

Give two numbers i will add and give the answer
Enter q to quit

Enter first number : 5
Enter second number : 4
This is the sum of two numbers 9

Enter first number : g
Enter second number : 5
Please enter two integers or float

Enter first number : q

Sorry the entered filename gopinath.txt doesn't exist


The book Alice_in_Wonderland.txt contains 29594 words in it 
"""
