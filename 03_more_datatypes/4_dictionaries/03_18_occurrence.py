'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

user_input = input("Please give me a string: ")
result = dict((letter,user_input.count(letter)) for letter in set(user_input))
print(result)