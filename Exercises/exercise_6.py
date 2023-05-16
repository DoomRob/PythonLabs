#!/usr/bin/env python3
def IsPrime(num): # If Statement to get the numbers that are prime
    for i in range(num):
        if num == 2 or num == 3 or num == 5:
            return True
        elif num % 2 == 0:
            return False
        elif num % 3 == 0:
            return False
        else:
            return True
# Loops through the numbers between 1 and 21       
for i in range(1, 21):
    if IsPrime(i + 1):
        print(i + 1, end=" ")
print() # Returns list