# Written: 11-Jan-2020
# https://www.hackerrank.com/challenges/30-arrays

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    print(' '.join([str(x) for x in arr[::-1]]))
    # print(' '.join(map(str, arr[::-1])))