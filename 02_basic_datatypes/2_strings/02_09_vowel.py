'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

# Get script from user

script = input("Please give me a sentence: ")

# Find total number of vowels

vowels = 0

for i in script:
    if (i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
        vowels = vowels + 1

print(vowels)

# Challenge...

a = 0
e = 0
eye = 0
o = 0
u = 0

for i in script:
    if (i == 'a' or i == 'A'):
        a = a + 1

    if (i == 'e' or i == 'E'):
        e = e + 1

    if (i == 'i' or i == 'I'):
        eye = eye + 1

    if (i == 'o' or i == 'O'):
        o = o + 1

    if (i == 'u' or i == 'U'):
        u = u + 1

print(f"There are {a} a's, {e} e's, {eye} i's, {o} o's and {u} u's!")



