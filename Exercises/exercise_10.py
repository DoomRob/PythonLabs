# Question 10:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in
# the i-th row and j-th column of the array should be i*j.
# Note: I = 0,1.., X-1; j=0,1,¡-Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
strInput = input("Enter two numbers: ") # Takes in two numbers
dim = [int(x) for x in strInput.split(",")] # Creates a array
irow = dim[0] 
jcol = dim[1]
superlist = [[0 for j in range(jcol)] for i in range(irow)]
for i in range(irow):
    for j in range(jcol):
        superlist[i][j] = i * j
superlist = [[i*j for j in range(jcol)] for i in range(irow)]
print(superlist)