"""
The first step in a merge sort is to separate the data into smaller lists. Then we break those lists into even smaller lists. 
Then, when those lists are all single-element lists, something amazing happens! Well, kind of amazing. 
Well, you might have expected it, we do call it a “merge sort”. We merge the lists.
"""
"""
How do we break up the data in a merge sort? We split it in half until there’s no more data to split.
Our first step is to break down all of the items of the list into their own list.
"""


def merge_sort(items):
    if len(items) <= 1:
        return items
    middle_index = len(items)//2
    left_split = items[:middle_index]
    right_split = items[middle_index:]
    return middle_index, left_split, right_split
