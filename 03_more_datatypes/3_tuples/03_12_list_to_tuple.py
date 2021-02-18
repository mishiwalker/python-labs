'''
Write a script that takes a list and turns it into a tuple.

'''

def convert(list_):
    return tuple(list_)

list_ = [item for item in input("Please give me a list: ").split()]

print(convert(list_))
