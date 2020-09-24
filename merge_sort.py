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
    left_sorted = merge_sort(left_split)
    right_sorted = merge_sort(right_split)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []
    while(left and right):
        if(left[0] < right[0]):
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    if(left):
        result += left
    if(right):
        result += right


"""
The whole sort takes up two functions:

merge_sort() which is called recursively breaks down an input list to smaller, more manageable pieces. 
merge() which is a helper function built to help combine those broken-down lists into ordered combination lists.

merge_sort() continues to break down an input list until it only has one element and then it joins that with 
other single element lists to create sorted 2-element lists. 
Then it combines 2-element sorted lists into 4-element sorted lists. 
It continues that way until all the items of the lists are sorted!

Only one thing left to do, test it out!
"""
unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19,
                   202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)
