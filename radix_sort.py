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

    """
    The least significant digit radix sort algorithm takes each number in the input list, 
    looks at the digits of that number in order from right to left, and incrementally 
    stuffs each number into the bucket corresponding to the value of that digit. First 
    we’re going to write this logic for the least significant digit, then we’re going 
    to loop over the code we write to do that for every digit.
    """

    for number in being_sorted:
        number_as_a_string = str(number)
        # get the last element of a string
        digit = number_as_a_string[-1]
        # use digit as a list index for digits
        digit = int(digit)
        """
        digits[digit] is an empty list (because digits has ten lists and digit is a number 
        from 0 to 9). Add our number to that list.
        """
        digits[digit].append(number)
    return digits


radix_sort()
