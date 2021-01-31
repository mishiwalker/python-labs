'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

#1 - convert an int to a float
a = 5
a = float(a)

#2 - convert a float to an int
a = int(a)

#3 - perform floor division using a float and an int
a = 10
b = 3.3
print(a//b)

#4 - use two user inputted values to perform multiplication
c = float(input("What is the first number you would like to multiply: "))
d = float(input("What is the second number you would like to multiply: "))
e = c * d
print(e)
