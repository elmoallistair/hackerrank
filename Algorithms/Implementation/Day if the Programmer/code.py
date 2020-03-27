# Written: 03-Jan-2020
# https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def dayOfProgrammer(year):
    # conditions
    con1 = year % 400 == 0
    con2 = year % 4 == 0
    con3 = year % 100 != 0
    if year == 1918:
        return '26.09.1918'
    elif (year <= 1917 and con2) or (year > 1918 and ((con1) or (con2 and con3)) ):
        return '12.09.{}'.format(year)
    else:
        return '13.09.{}'.format(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    year = int(input().strip())
    result = dayOfProgrammer(year)
    fptr.write(result + '\n')
    fptr.close()
