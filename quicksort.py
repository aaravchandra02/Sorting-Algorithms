"""
We’ll use two pointers, start and end to keep track of sub-lists in our algorithm.

"""
from random import randrange


def quicksort(list, start, end):
    if start >= end:
        return
    print(list[start])
    pivot_idx = randrange(start, end)
    pivot_element = list[pivot_idx]
    start += 1
    quicksort(list, start, end)


colors = ["blue", "red", "green", "purple", "orange"]
quicksort(colors, 0, len(colors)-1)
my_list = [32, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)
