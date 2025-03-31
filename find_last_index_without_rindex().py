# find last index without rindex()
# this program will return the first location of the function parameter in the string starting from the last character

# ask the user for a string and a substring to find
string = input("Enter a string: ")
substring = input("Enter a substring to find: ")

# iterate throught the string in reverse, checking for the first occurence of the substring
for index in range(len(string) - 1, -1, -1):
    if string[index:index + len(substring)] == substring:
        # if found, print the index and break the loop
        print(index)
        break

# if not found, print a message indicating that
else: 
    print("Substring not found in the string")