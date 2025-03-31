# find first index without index()
# this program will return the first location of the function parameter in the string

# ask the user for a string and a substring to find
string = input("Enter a string: ")
substring = input("Enter a substring to find: ")

# iterate though the string, checking for the first occurence of the substring
for index in range(len(string)):
    if string[index:index + len(substring)] == substring:
        # if found, print the index and break the loop
        print(index)
        break

# if not found, print a message indicating that
else:
    print("Substring not found in the string.")