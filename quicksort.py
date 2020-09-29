"""
We’ll use two pointers, start and end to keep track of sub-lists in our algorithm.

"""
from random import randrange


def quicksort(listl, start, end):
    if start >= end:
        return listl

    pivot_idx = randrange(start, end)
    pivot_element = listl[pivot_idx]
    listl[end], listl[pivot_idx] = listl[pivot_idx], listl[end]

    # Create the lesser_than_pointer
    lesser_than_pointer = start
    # Start a for loop, use 'idx' as the variable
    for idx in range(start, end):
        if listl[idx] < pivot_element:
            listl[lesser_than_pointer], listl[idx] = listl[idx], listl[lesser_than_pointer]
            lesser_than_pointer += 1
    listl[end], listl[lesser_than_pointer] = listl[lesser_than_pointer], listl[end]
    print(listl[start])
    start += 1
    return quicksort(listl, start, end)


colors = ["blue", "red", "green", "purple", "orange"]
quicksort(colors, 0, len(colors)-1)
my_list = [32, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)
my_list = [42, 103, 22]
print("BEFORE: ", my_list)
sorted_list = quicksort(my_list, 0, len(my_list) - 1)
print("AFTER: ", sorted_list)
