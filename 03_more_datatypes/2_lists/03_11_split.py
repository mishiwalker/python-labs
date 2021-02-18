'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

og_list = [item for item in input("Please give me a sentence: ").split()]

def most_frequent(og_list):
    return max(set(og_list), key = og_list.count)

print(most_frequent(og_list))