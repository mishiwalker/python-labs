'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

# Take a string of words from user

sentence = input("Please give me a sentence: ")

# Take a letter from the user

letter = input("Give me a letter within the first sentence: ")

# Find the first occurence of the letter in the string

print (sentence.find(letter))





