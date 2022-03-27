# simple program with while loop and inputs to check try and except FileNotFoundError,
# if succeeds print number of words in the file


def count_no_of_words(file_name):
    try:
        with open(file_name, encoding='utf-8') as txt:
            content = txt.read()
    except FileNotFoundError:
        print(f"\nSorry the entered filename {file_name} doesn't exist")
    else:
        words = content.split()
        num_words = len(words)
        print(f"\n\nThe file {file_name} contains {num_words} words in it")


file_name = 'gopi.txt'
count_no_of_words(file_name)
file_name = 'Alice_in_Wonderland.txt'
count_no_of_words(file_name)

#output
"""
The file gopi.txt contains 32 words in it
The file Alice_in_Wonderland.txt contains 29594 words in it
"""
