"""
The first step in a merge sort is to separate the data into smaller lists. Then we break those lists into even smaller lists. 
Then, when those lists are all single-element lists, something amazing happens! Well, kind of amazing. 
Well, you might have expected it, we do call it a “merge sort”. We merge the lists.
"""
"""
How do we break up the data in a merge sort? We split it in half until there’s no more data to split.
Our first step is to break down all of the items of the list into their own list.
"""
"""
Our merge_sort() function so far only separates the input list into many different parts — 
pretty much the opposite of what you’d expect a merge sort to do.
To actually perform the merging, we’re going to define a helper function that joins the data together.
"""

"""
Now we need to build out our result list. When we’re merging our lists together, 
we’re creating ordered lists that combine the elements of two lists.
"""


def merge_sort(items):
    if len(items) <= 1:
        return items
    middle_index = len(items)//2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    return middle_index, left_split, right_split


def merge(left, right):
    result = []
    while(left and right):
        if(left[0] < right[0]):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
