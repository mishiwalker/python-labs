'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

guest = "Luke SkyWalker"

def origrate(num):
    rate1 = 90
    return rate1

def discount(nums):
    disc = 30
    return disc

def diff(num):
    difference = origrate(100) - discount(30)
    return difference

firstrate = origrate(0)
secondrate = diff(0)
discounted = discount(0)

print(f"Dear {guest}, your discounted rate is {secondrate}, which is down from {firstrate} which equals a discount of {discounted}")
