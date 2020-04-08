# Written: 09-Apr-2020
# https://www.hackerrank.com/challenges/counting-valleys/problem?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    count = hike = 0
    for i in range(len(s)):
        if s[i] == 'U':
            count += 1
            if count == 0:
                hike += 1
        else:
            count -= 1
        
    return(hike)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
