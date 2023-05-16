# Question 14:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def even(n1, n2):
    range_numbers = range(n1, n2)
    result = []
    for i in range_numbers: # Prints numbers that are even and prints them out between 1000 and 3000
        if i % 2 == 0:
            result.append(i)
    return print(result)
(even(1000, 3001)) # Returns Results
            
        