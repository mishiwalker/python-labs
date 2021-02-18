'''
Write a script that takes a tuple and turns it into a list.

'''

tuple_ = tuple(input("Please give me a tuple: "))
list_ = [item for x in tuple_ for item in tuple_]
print(list_)