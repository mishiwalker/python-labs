'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list):
  max_ = max(example_list)
  min_ = min(example_list)
  avg_ = sum(example_list) / len(example_list)
  sum_ = sum(example_list)
  return max_, min_, avg_, sum_

  # define the function here
def_stats = stats(example_list)

# call the function below here and print original list
print(example_list)
print(def_stats)
