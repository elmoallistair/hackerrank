# Written: 14-Jan-2020
# https://www.hackerrank.com/challenges/30-2d-arrays

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    arrsum = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for row in range(len(arr) - 2):
        for col in range(len(arr[row]) - 2):
            a = int(arr[row][col])
            b = int(arr[row][col+1])
            c = int(arr[row][col+2])
            d = int(arr[row+1][col+1])
            e = int(arr[row+2][col])
            f = int(arr[row+2][col+1])
            g = int(arr[row+2][col+2])
            sum = a + b + c + d + e + f + g
            arrsum.append(sum)
    print(arrsum)
    print(max(arrsum))