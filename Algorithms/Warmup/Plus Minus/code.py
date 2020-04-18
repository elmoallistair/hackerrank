# Written: 15-Dec-2019
# https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count_pos = count_neg = count_zero = 0
    for num in arr:
        if num > 0:
            count_pos += 1
        elif num < 0:
            count_neg += 1
        else:
            count_zero += 1

    print(count_pos/n)
    print(count_neg/n)
    print(count_zero/n)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)