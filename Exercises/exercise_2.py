# Question 2
# Write a program which can compute the factorial of a given number.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
# Hints:
# e.g Factorial 8 is calculated as 8x7x6x5x4x3x2x1
# In case of input data being supplied to the question, it should be assumed to be a console
# input 

#!/usr/bin/env python3
def factorial():
    n = int(input("Please enter a new number: ")) # Takes input from the user
    factorial = 1
    results = [] # Lists the number from the input
    for i in range(n, 0, -1):
        factorial = factorial * i
        results.append(str(factorial))
    print(results)
factorial() # Returns the results

        



