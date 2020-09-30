def radix_sort(to_be_sorted):
    # In order to determine how many digits are in the longest number in the list,
    # we’ll need to find the longest number.
    maximum_value = max(to_be_sorted)

    max_exponent = len(str(maximum_value))
    return max_exponent
