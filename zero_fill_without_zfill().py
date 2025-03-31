# zero fill without zfill()
# this program add zero characters at the beginning of the string to complete the number of characters specifies in function parameter

# ask the user for a string and a width 
string = input("Enter a string: ")
width = int(input("Enter the width: "))

# calculate the number of zeros needed to reach the desired width
num_zeros = width - len(string)

# print the zeros followed by the string
print('0' * num_zeros + string, end='')