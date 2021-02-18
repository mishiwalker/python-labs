'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
numlist = list(input("Please give me 10 numbers: "))
numlist.sort()
print(numlist[-1])

# Challenge - first converted list to int

nums = [int(i) for i in numlist]

sum = 0
for x in nums:
    sum = sum + x
print(sum)