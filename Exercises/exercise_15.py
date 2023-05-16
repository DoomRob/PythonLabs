# Question 15:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
sentence = input("Enter a line ") # Takes the user input
data = {"DIGITS":0, "LETTERS":0} # Prints the amount of digits and letters
for c in sentence:
    if c.isdigit():
        data["DIGITS"]+=1
    elif c.isalpha():
        data["LETTERS"]+=1
    else:
        pass
print("LETTERS", data["LETTERS"]) # Outputs the results
print("DIGITS", data["DIGITS"]) # Outputs the results