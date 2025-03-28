# check if ends with without endswith
# this program will check if the string end part matches the function parameter

# ask user for input and a suffix
string = input("Enter a string: ")
suffix = input("Enter a suffix: ")

# compare the last character of the string with the suffix
print(string[-len(suffix):] == suffix)  # check if the last part of the string matches the suffix
# if the string ends with the suffix, the program will print True