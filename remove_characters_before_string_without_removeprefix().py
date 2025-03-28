# remove characters before string without removeprefix
# this program will remove characters at the beginning of a string without removeprefix

# ask the user for a string and a prefix
string = input("Enter a string: ")
prefix = input("Enter a prefix: ")

if string.startswith(prefix): # check if the prefix is in the string
    print(string[len(prefix):])  # if it is, remove the prefix from the string

else: # otherwise, print the string as is
    print(string) 
