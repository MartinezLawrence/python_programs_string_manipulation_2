# convert uppercase without upper()
# this program converts all characters of the string into upper case without upper() function.

# ask the user for a string
string = input("Enter a string: ")

# initialize an empty string to store the result
result = ""

# iterate through each character in the string
for char in string:
    if 'a' <= char <= 'z':
        # if the character is lowercase, convert it to uppercase by subtracting 32 from its ASCII value
        result += chr(ord(char) - 32)
    else: 
        # if the character is already uppercase, append it as it is
        result += char        

# print the result string
print(result)