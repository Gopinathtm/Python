# Sample program to open and get data from files at different locations
# opening a file from sampe python folder and appending these lines to it
with open('gopi.txt', 'a')as file_object:
    lines = file_object.write('\nI am adding a extra line through pyhton\n')
    line = file_object.write('let see if it does not replace the old one\n')
    print(lines)
    
# opening a file from another sub folder
with open('txt_files/my_name.txt') as name_file:
    y = name_file.read()
    print(y)
    
    
# opening a file from desktop location
file_path = '/Users/admin/Desktop/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.readlines()
    print(contents)
    pi_string = ''
    for content in contents:
        pi_string += content.strip()
    print(pi_string)
    print(len(pi_string))
 # converting the contents of file to float
g = float(pi_string)
f = g * 4
print(f)
# calling contents of the file outside the block
print(lines)
