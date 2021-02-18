'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
numbers = (list(input("Please give me 6 numbers: ")))
numbers2 = [int (x) for x in numbers]
list.sort(numbers2)
numbers3 = (tuple(numbers2[0:2]))
numbers4 = (tuple(numbers2[2:4]))
numbers5 = (tuple(numbers2[4:6]))
last_number = numbers2[-1]
odd_num = (last_number, 0)

if len(numbers2) % 2 == 0:
    print(numbers3)
    print(numbers4)
    print(numbers5)
else:
    print(numbers3)
    print(numbers4)
    print(numbers5)
    print(odd_num)
