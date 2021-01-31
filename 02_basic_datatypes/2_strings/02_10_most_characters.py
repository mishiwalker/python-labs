'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

print("Give me three words:")
word1 = input("First word: ")
word2 = input("Second word: ")
word3 = input("Third word: ")

w1l = len(word1)
w2l = len(word2)
w3l = len(word3)

print(w1l, word1)
print(w2l, word2)
print(w3l, word3)

# Challenge

if w1l > w2l and w1l > w3l:
    print(word1)

if w2l > w1l and w2l > w3l:
    print(word2)

if w3l > w1l and w3l > w2l:
    print(word3)


