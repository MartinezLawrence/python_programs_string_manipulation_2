# swap case without swapcase()
# this program will reverse the casing of each of the character of the string

# ask the user for a string
string = input("Enter a string: ")

# initialize an empty string result
result = ""

# iterate through each character in the string
for char in string:
    # if the character is uppercase, convert it to lowercase and add it to result
    if 'A' <= char <= 'Z': 
        result += char.lower()

    # if the character is lowercase, convert it to uppercase and add it to result
    elif 'a' <= char <= 'z':
        result += char.upper()
    
    # if the character is neither, just add it to result
    else:
        result += char

# print the result
print(result, end="")