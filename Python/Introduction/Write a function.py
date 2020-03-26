# Written: 04-Jan-2020
# https://www.hackerrank.com/challenges/write-a-function

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