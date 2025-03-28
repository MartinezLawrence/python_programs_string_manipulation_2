# capitalize without capitalize()
# this program will makes the first letter of the string capital letter

# ask the user for a string
string = input("Enter a string: ")

# check if the string is empty
if string: 
    print(string[0].upper() + string[1:].lower(), end="")

# if not empty, convert the first letter to uppercase and the rest to lowercase
else: 
    print(string, end="")   # # print the result
