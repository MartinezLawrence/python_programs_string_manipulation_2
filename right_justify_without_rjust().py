# right justify without rjust()
# this program add space characters at the beginning of the string to complete the number of characters specifies in function parameter

# ask user for a string and a width
string = input("Enter a string: ")
width = int(input("Enter the width: "))

# calculate the number of spaces needed to reach the desired width
print(' ' * (width - len(string)) + string, end='')    # print spaces followed by the string