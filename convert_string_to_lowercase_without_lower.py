# convert string into lowercase without lower
# this program will convert strings into lowercase without lower

# ask user for a string
string = input("Enter a string: ")

# initialize an empty string result
result = ""

# iterate through each character in the string
for char in string: 
    if 'A' <= char <= 'Z':      # check if the character is uppercase
        result += chr(ord(char) + 32)
    else:                       # otherwise, keep it as is
        result += char        

# print the result
print(result) 
