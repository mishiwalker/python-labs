'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''
# there are two ways to solve this:
star = '*'
# if i want the user to specify what n is, i could use:
  # n = int(input("Give me a number between 1 - 10: "))
# but in this instance, we know what n is (5)
n = 5
m = 1
while n > 0:
    print(star * m)
    n -= 1
    m += 1

# or I can use:

for y in range(6):
    print("*" * y)


