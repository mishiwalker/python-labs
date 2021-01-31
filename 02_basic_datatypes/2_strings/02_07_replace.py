'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# Get sentence from user:

sentence = input("Please enter a sentence: ")

# Get symbol from user:

char = input("Please enter a symbol: ")

# Get first letter of sentence

first = sentence[0]

# Replace all occurences of the first letter with the symbol

print(sentence.replace(first, char))
