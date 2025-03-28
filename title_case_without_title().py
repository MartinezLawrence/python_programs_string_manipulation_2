# title case without title()
# this program will makes all first letter of each word in the string capital letter

# ask the user for a string
string = input("Enter a string: ")

# split the string into words
words = string.split()

# for each word, capitalize the first letter and make the rest lowercase
print(' '.join(word.capitalize() for word in words), end="")  # join the words together and print the result

