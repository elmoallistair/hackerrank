# Written: 12-Jan-2020
'''
* Resources: https://www.hackerrank.com/challenges/30-recursion/tutorial
*
* Task
*   Write a factorial function that takes a positive integer, N as a parameter and prints the result of N! (N factorial).
*   Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of 0.
*
* Input Format
*   A single integer, N (the argument to pass to factorial).
*
* Constraints
*   - 2 <= N <= 12
*   - Your submission must contain a recursive function named factorial.
*
* Output Format
*   Print a single integer denoting N!.
*
* Sample Input
*   3
*
* Sample Output
*   6
*
* Explanation
*   Consider the following steps:
*   1. factorial(3) = 3 x factorial(2)
*   2. factorial(2) = 2 x factorial(1)
*   3. factorial(1) = 1
*   From steps 2 and 3, we can say factorial(2) = 2 x 1 = 2;
*   then when we apply the value from factorial(2) to step 1, we get factorial(3) = 3 x 2 x 1 = 6.
*   Thus, we print 6 as our answer.
'''

# ===============================================

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
