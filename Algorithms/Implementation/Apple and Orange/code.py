# Written: 02-Jan-2020
# https://www.hackerrank.com/challenges/apple-and-orange/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ap_count = or_count = 0
    for i in apples:
        fall_loc = a + i
        if s <= fall_loc <= t:
            ap_count += 1
    for i in oranges:
        fall_loc = b + i
        if s <= fall_loc <= t:
            or_count += 1

    # Shorter Code:
    # ap_count = len([i for i in apples if s <= a+i <=t])
    # or_count = len([i for i in oranges if s <= b+i <=t])

    print(ap_count)
    print(or_count)

if __name__ == '__main__':
    st = input().split()
    s = int(st[0])  # Starting point
    t = int(st[1])  # Ending Point

    ab = input().split()
    a = int(ab[0])  # Location of the Apple tree
    b = int(ab[1])  # Location of the Orange tree

    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split())) 
    oranges = list(map(int, input().rstrip().split())) 

    countApplesAndOranges(s, t, a, b, apples, oranges)


