#!/usr/bin/env python3
def IsYearLeap(year):
    # If Statement
    if year % 4 == 0 and year % 100 != 0: # If the year is a leap year
        return True
        print("It is leap a year")
    elif year % 400 == 0: # If the year is a leap year
        return True
        print("It's a leap year")
    else: # Defaults to a common year
        return False

testdata = [1900, 2000, 2016, 1987] # The years that will be used as test data
testresults = [False, True, True, False] # The results that I being used
for i in range(len(testdata)):
    yr = testdata[i]
    print(yr,"->",end="")
    result = IsYearLeap(yr)
    if result == testresults[i]: # An if statement that will confirm if the test data is a sucess or not.
        print("OK")
    else:
        print("Failed")