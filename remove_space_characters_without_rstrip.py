# remove space characters without rstrip 
# this program will remove the space characters at the end of the string without rstrip

# ask the user for a string
string = input("Enter a string: ")

# initialize a pointer last_char to the last character of the string
last_char = len(string) - 1

# while last_char is greater than or equal to 0 and the character at last_char is a space
while last_char >= 0 and string[last_char] == ' ':
    # decrement last_char by 1
    last_char -= 1

# print the string from the beginning to last_char + 1
print(string[:last_char + 1])