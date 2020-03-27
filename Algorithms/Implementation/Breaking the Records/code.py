# Written: 03-Jan-2020
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    high = scores[0]    # Temporary highest score
    low = scores[0]     # Temporary Lowest score
    h_count = l_count = 0

    for i in range(len(scores)):
        if scores[i] > high:
            high = scores[i]
            h_count += 1
        if scores[i] < low:
            low = scores[i]
            l_count += 1

    return(h_count, l_count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
