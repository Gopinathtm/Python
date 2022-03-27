# simple program with while loop and inputs to check try and except FileNotFoundError,
# loop in list of file names if succeeds print number of words in the file

def count_no_of_words(file_name):
    try:
        with open(file_name, encoding='utf-8') as txt:
            content = txt.read()
    except FileNotFoundError:
        print(f"Sorry the entered filename {file_name} doesn't exist")
    else:
        words = content.split()
        num_words = len(words)
        print(f"The file {file_name} contains {num_words} words in it")


file_name = ['gopi.txt', 'little_women.txt', 'Alice_in_Wonderland.txt', 'Moby-Dick.txt']
for file_nam in file_name:
    count_no_of_words(file_nam)
    
# output
"""
The file gopi.txt contains 32 words in it
Sorry the entered filename little_women.txt doesn't exist
The file Alice_in_Wonderland.txt contains 29594 words in it
The file Moby-Dick.txt contains 215711 words in it
"""
