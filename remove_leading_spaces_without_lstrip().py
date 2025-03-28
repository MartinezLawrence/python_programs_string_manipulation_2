# remove leading spaces without lstrip
# this program will remove leading spaces without lstrip

# ask the user to enter a string
string = input("Enter a string with leading spaces: ")

# initialize a pointer to 0 
pointer = 0

# if the pointer is less than the length of the string and the character at the pointer is a space
while pointer < len(string) and string[pointer] == ' ':
    pointer += 1 # increment the pointer

# print the string without leading spaces
print(string[pointer:]) # print the string from the pointer to the end of the string
