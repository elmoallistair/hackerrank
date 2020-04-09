# Written: 09-Apr-2020
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < n-1:
        if i+2 >= n or c[i+2] == 1:
            count += 1
            i += 1
        else:
            count += 1
            i += 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
