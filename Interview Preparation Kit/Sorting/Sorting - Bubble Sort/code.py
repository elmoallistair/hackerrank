# Written: 30-Apr-2020
# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    counter = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                counter += 1

    print('Array is sorted in {} swaps.'.format(counter))
    print('First Element:', a[0])
    print('Last Element:', a[-1])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
