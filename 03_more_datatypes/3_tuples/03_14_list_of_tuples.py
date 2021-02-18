'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

string_ = input("Please give me a string: ")
list_ = string_.split()
result = list(map(tuple, list_))
print(result)