'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

result = {"a": 3, "b": 2, "c": 7 , "d": 2}

'''

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}
dict_3 = {}

for v, x in dict_1.items():
    for y, z in dict_2.items():
        if v == y:
            dict_3[v] = x + z
        elif v not in dict_2 and v not in dict_3:
            dict_3[v] = x
        elif y not in dict_1 and y not in dict_3:
            dict_3[y] = z

print(dict_3)

