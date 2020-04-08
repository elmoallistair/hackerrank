# Written: 08-Apr-2020
# https://www.hackerrank.com/challenges/array-left-rotation/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def solution(arr, d):
    for i in range(d):
        arr.append(arr[0])
        arr.remove(arr[0])

    print(*arr)

if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    solution(a, d)
