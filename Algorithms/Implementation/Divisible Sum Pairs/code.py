# Written: 03-Jan-2020
# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    pairs = 0
    for i in range(len(ar)):
        for j in range(i+1, len(ar)):
            # Check if  ar[i]+ar[j] is evenly divisible by k.
            if (ar[i]+ar[j])%k == 0:
                pairs += 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
