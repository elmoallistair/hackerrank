# Written: 15-Jan-2020
# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

import numpy as np
from scipy import stats

N = int(input())
arr = list(map(int, input().split()))

print(np.mean(arr))
print(np.median(arr))
print(int(stats.mode(arr)[0]))