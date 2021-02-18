'''
Take two numbers from the user, one representing the start and one the end of a sequence.
Using a loop, sum all numbers from the first number through to the second number.

For example, if a user enters 1 and 100, the sequence would be all integer numbers from 1 to 100.
The output of your calculation should therefore look like this:

The sum is: 5050
'''

num1 = int(input("Please give me the first number: "))
num2 = int(input("Please give me the second number: "))
num3 = num2 + 1
num4 = sum(x for x in range(num1, num3))

print(num4)