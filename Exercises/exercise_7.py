#!/usr/bin/env python3
# Question 7:
# With a given integer n, write a program to generate a dictionary that contains (i, i*i) such that i is an
# integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()
def the_dict(the_dict): # Function
    the_dict = {n: n**2 for n in [1,2,3,4,5,6,7,8]} # Takes each number and * by two
    print(the_dict)
the_dict(the_dict) # Return answer
    
    
