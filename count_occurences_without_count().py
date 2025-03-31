# count occurences without count() 
# this program return how many time the function parameter appear in the string

# ask the user for a string and a substring to count
string = input("Enter a string: ")
substring = input("Enter a substring to count: ")
count = 0       # initialize a counter count to 0
unique = 0

# iterate through the string, checking for occurences of the substring
while unique < len(string): 
    if string [unique:unique + len(substring)] == substring:
        count += 1      # if found, increment count
        unique += len(substring)
    else:
        unique += 1

# print count
print(count)
