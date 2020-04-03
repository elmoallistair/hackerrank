# Written: 21-Jan-2020
# https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new_s = list()
    for i in range(len(s)):
        if (i == 0 or s[i-1] == ' '):
            new_s.append(s[i].upper())
        else:
            new_s.append(s[i])
    return ''.join(new_s)
    # return ''.join([s[i].upper() if (i == 0 or s[i-1] == ' ') else s[i] for i in range(len(s))])

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
