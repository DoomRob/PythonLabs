#!/usr/bin/env python3
def IsYearLeap(year):
    # If Statement
    if year % 4 == 0 and year % 100 != 0: # If the year is a leap year
        return True
        print("It is a leap year")
    elif year % 400 == 0: # If the year is a leap year
        return True
    else: # Defaults 
        return False

def DaysInMonth(year,month): # Used to loop through the months   
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        leapyear = IsYearLeap(year) # If the year is a leap year then Febuary returns 29 days
        if leapyear == True:
            return 29
        else:
            return 28

# The years that will be used as test data
testyears = [1900, 2000, 2016, 1987]
testmonths = [ 2, 2, 1, 11]
testresults = [28, 29, 31, 30]
for i in range(len(testyears)): # The results that I being used
    yr = testyears[i]
    mo = testmonths[i]
    print(yr,mo,"->",end="")
    result = DaysInMonth(yr,mo)
    if result == testresults[i]: # An if statement that will confirm if the test data is a sucess or not.
        print("OK")
    else:
        print("Failed")