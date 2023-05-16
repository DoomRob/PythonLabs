# Question 12
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
some_lines = []
while True:
    words = input()
    if words:
        some_lines.append(words.upper())
    else:
        break

for sen in some_lines:
    print(sen)