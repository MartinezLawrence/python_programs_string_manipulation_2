# check if All Lowercase Without islower()
# This program checks if all characters in a string are lowercase letters

# Ask the user for a string
string = input("Enter a string: ")

# Initialize a flag all_lowercase to True
all_lowercase = True

# Iterate through each character in the string
for char in string:
    # Check if the character is an uppercase letter
    if 'A' <= char <= 'Z':
        # If it is, set all_lowercase to False and break the loop
        all_lowercase = False
        break

# Print whether all_lowercase is True or False
print(all_lowercase)