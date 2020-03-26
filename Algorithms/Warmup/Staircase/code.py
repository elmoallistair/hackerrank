# Written: 31-Dec-2019
# https://www.hackerrank.com/challenges/staircase/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    row = ''
    for i in range(1, n+1):
        row = ' '*(n-i) + '#'*i
        print(row)
    staircase(n)
