def radix_sort(to_be_sorted):
    # In order to determine how many digits are in the longest number in the list,
    # we’ll need to find the longest number.
    maximum_value = max(to_be_sorted)

    max_exponent = len(str(maximum_value))
    """
    By the nature of a radix sort we need to erase and rewrite our output list 
    a number of times. It would be bad practice to mutate the input list
    """
    # create copy of to_be_sorted here
    being_sorted = to_be_sorted[:]

    """
    A radix sort goes through each position of each number and puts all of the 
    inputs in different buckets depending on the value . Since there are 10 
    different values (that is, 0 through 9) that a position can have, we need 
    to create ten different buckets to put each number in.
    """
    digits = [[] for _ in range(10)]
    print(digits)
    return digits


radix_sort()
