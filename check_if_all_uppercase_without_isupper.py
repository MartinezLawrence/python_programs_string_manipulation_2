# check if all uppercase without isupper
# this program will check if all characters is on uppercase without isupper()

# ask the user for a string
string = input("Enter a string: ")

# initialize a flag all_uppercase to True
all_uppercase = True

# iterate through each character in the string
for char in string: 
    if 'a' <= char <= 'z':
        all_uppercase = False  # if the character is lowercase, set all_uppercase to False
        break

# print whether all_uppercase is True or False
print(all_uppercase)