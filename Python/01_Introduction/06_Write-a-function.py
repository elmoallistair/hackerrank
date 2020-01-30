# Written: 04-Jan-2020
'''
* Resource: https://www.timeanddate.com/date/leapyear.html
*
* Task
*   You are given the year, and you have to write a function to check if the year is leap or not.
*   Note that you have to complete the function and remaining code is given as template.
*
* Input Format
*   Read y, the year that needs to be checked.
*
* Constraints
*   1900 <= y <= 10**5
*
* Output Format
*   Output is taken care of by the template. Your function must return a boolean value (True/False)
*
* Sample Input 0
*   1990
*
* Sample Output 0
*   False
*
* Explanation 0
*   1990 is not a multiple of 4 hence it's not a leap year.
'''

# ===============================================

def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 != 0:
            return True
    return False

    # Shorter Code:
    # return (year%4 == 0) and ((year%400 == 0) or (year%100 != 0))

year = int(input())
print(is_leap(year))