"""
We’ll use two pointers, start and end to keep track of sub-lists in our algorithm.

"""
from random import randrange, shuffle


def quicksort(listl, start, end):
    if start >= end:
        return listl

    pivot_idx = randrange(start, end+1)
    pivot_element = listl[pivot_idx]
    listl[end], listl[pivot_idx] = listl[pivot_idx], listl[end]

    # Create the lesser_than_pointer
    lesser_than_pointer = start
    # Start a for loop, use 'idx' as the variable
    for i in range(start, end):
        if listl[i] < pivot_element:
            listl[lesser_than_pointer], listl[i] = listl[i], listl[lesser_than_pointer]
            lesser_than_pointer += 1
    listl[end], listl[lesser_than_pointer] = listl[lesser_than_pointer], listl[end]
    # Call quicksort on the "left" and "right" sub-lists
    quicksort(list, start, lesser_than_pointer - 1)
    quicksort(list, lesser_than_pointer + 1, end)
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
unsorted_list = [3, 7, 12, 24, 36, 42]
shuffle(unsorted_list)
print(unsorted_list)
# use quicksort to sort the list, then print it out!

quicksort(unsorted_list, 0, len(unsorted_list) - 1)
print(unsorted_list)
