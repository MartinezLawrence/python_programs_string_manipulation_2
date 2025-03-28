# center without center()
# this program will add space characters at the beginning and at the end of the string to print the string at the center

# ask the user for a string and a width
string = input("Enter a string: ")
width = int(input("Enter the width: "))

# calculate the total number of spaces needed to center the string
spaces = width - len(string)

# divide these spaces evenly between the left and right sides
left_spaces = spaces // 2
right_spaces = spaces - left_spaces

# print the left spaces, the string, and the right spaces altogether
print(" " * left_spaces + string + " " * right_spaces, end="")