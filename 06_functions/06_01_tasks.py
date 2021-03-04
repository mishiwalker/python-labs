'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
divnum = int(input("Please give me a number between 1 and 1,000,000,000: "))

def divis1(number):
    if divnum % 4 == 0 or divnum % 7 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def divis2(number):
    if divnum % 4 == 0 and divnum % 7 == 0:
        return True
    else:
        return False

# take in a number from the user between 1 and 1,000,000,000


# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
number = divis1(divnum)
number2 = divis2(divnum)

# print your new variables to display the results
print(number)
print(number2)