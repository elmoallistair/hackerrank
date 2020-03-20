# Written: 12-Dec-2019
'''
* Calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
*
* Function Description
*   Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.
*   aVeryBigSum has the following parameter(s):
*     - ar: an array of integers .
'''

# ===============================================

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()
