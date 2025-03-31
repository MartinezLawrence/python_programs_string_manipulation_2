# remove suffix without removesuffix()
# this program will remove the characters at the end of the string that matches the function parameter

# Ask the user for a string and a suffix.
string = input("Enter a string: ")
suffix = input("Enter a suffix: ")

# Check if the string ends with the given suffix.
if string.endswith(suffix):
    # If it does, print the substring from the start of the string to the beginning of the suffix.
    print(string[:-len (suffix)])

else:   #  otherwise, print the original string.
    print(string) 