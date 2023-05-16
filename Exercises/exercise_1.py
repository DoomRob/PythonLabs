#!/usr/bin/env python3
def divideseven(n1, n2):
    # create a range of numbers from n1 to n2 (excluding n2)
    range_numbers = range(n1, n2)
    # create an empty list to store the result
    result = []
    # iterate over the range of numbers
    for number in range_numbers:
        # iterate over the range of numbers
        if number % 7 == 0 and number % 5 != 0:
            # if the condition is True, append the number to the result list
            result.append(number)
            # print the result list
    return print(result)
# call the divideseven function with arguments 2000 and 3201
(divideseven(2000, 3201))

    

