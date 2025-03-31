# check starts with without startswith()
# this program check if the string beginning part matches the function parameter

# ask the user for a string and a prefix
string = input("Enter a string: ")
prefix = input("Enter a prefix: ")

# compare the first 'n' characters of the string with the prefix(n = lenght of prefix)
print((string[:len(prefix)]) == prefix)   # print whether they match