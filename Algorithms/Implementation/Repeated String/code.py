# Written: 10-Apr-2020
# https://www.hackerrank.com/challenges/repeated-string/problem?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    temp = s.count('a') * (n//len(s))
    remainder = s[:n%len(s)].count('a')

    return temp+remainder
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
