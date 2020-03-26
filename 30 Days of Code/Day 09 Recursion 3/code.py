# Written: 12-Jan-2020
# https://www.hackerrank.com/challenges/30-recursion

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return n
    else:
        return (n*(factorial(n-1)))

    # Shorter Code:
    # return n if n == 1 else (n*(factorial(n-1)))
if __name__ == '__main__':
    n = int(input())        # 2 <= n <= 2
    result = factorial(n)
    print(result)
