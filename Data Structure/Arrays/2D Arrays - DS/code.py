# Written: 29-Mar-2020
# https://www.hackerrank.com/challenges/2d-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass = list()
    for row in range(len(arr)-2):
        sum = 0
        for col in range(len(arr[row])-2):
            a = arr[row][col]
            b = arr[row][col+1]
            c = arr[row][col+2]
            d = arr[row+1][col+1]
            e = arr[row+2][col]
            f = arr[row+2][col+1]
            g = arr[row+2][col+2]
            sum = a+b+c+d+e+f+g
            hourglass.append(sum)
    return max(hourglass)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
