# Written: 03-Jan-2020
# https://www.hackerrank.com/challenges/the-birthday-bar

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    pieces = 0
    for i in range(len(s)):
        n = 0
        count = 0
        for j in range(n,m):
            if i+j == len(s):
                break
            count += s[i+j]
        if count == d:
            pieces += 1
    return pieces

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    result = birthday(s, d, m)
    print(result)
