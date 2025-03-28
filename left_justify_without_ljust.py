# left justify without ljust
# this program will add space characters at the end of the string to complete the number of characters specifies in function parameter

# ask the user for the string and a width
string = input("Enter a string: ")
width = int(input("Enter the width: "))

# calculate the number of spaces needed to reach the desired width
print(string + " " * (width - len(string)), end="")    # print the string with the spaces followed by the spaces