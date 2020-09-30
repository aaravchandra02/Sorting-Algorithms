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

    """
    For every iteration, radix sort renders a version of the input list that is sorted based on
    the digit that was just looked at. At first pass, only the ones digit is sorted. At the second 
    pass, the tens and the ones are sorted. This goes on until the digits in the largest position 
    of the largest number in the list are all sorted, and the list is sorted at that time.
    Here we’ll be rendering the list, at first, it will just return the list sorted so just the ones 
    digit is sorted.

    Since we know that all of our input numbers are in digits we can safely clear out being_sorted. 
    We’ll make it an empty list and then add back in all the numbers from digits as they appear.
    """

    being_sorted = []
    # Call each of these lists numeral because they each correspond to one specific numeral from 0 to 9
    for numeral in digits:
        # use the .extend() method (which appends all the elements of a list,
        # instead of appending the list itself) to add the elements of numeral to being_sorted
        being_sorted.extend(numeral)
    return being_sorted


radix_sort()
