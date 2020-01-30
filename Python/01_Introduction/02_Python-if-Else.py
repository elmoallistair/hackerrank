# Written : 04-Jan-2020
'''
* Resource: https://www.hackerrank.com/challenges/py-if-else/tutorial
*
* Task
*   Given an integer, n, perform the following conditional actions:
*   - If n is odd, print Weird
*   - If n is even and in the inclusive range of 2 to 5, print Not Weird
*   - If n is even and in the inclusive range of 6 to 20, print Weird
*   - If n is even and greater than 20, print Not Weird
*
* Input Format
*   A single line containing a positive integer, n.
*
* Constraints
*   1 <= n <= 100
*
* Output Format
*   Print Weird if the number is weird; otherwise, print Not Weird.
*
* Sample Input 0
*   3
*
* Sample Output 0
*   Weird
'''

# ===============================================

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())  # Constraints: 1 <= n <= 100

    if n%2 == 1:    # If n is odd
        print('Weird')
    elif n%2 == 0:  # If n is even ...
        # ...and in the inclusive range of 2 to 5
        if n in range(2, 5+1):
            print('Not Weird')
        # ...and in the inclusive range of 6 to 20
        elif n in range(6, 20+1):
            print('Weird')
        # ...and greater than 20
        elif n > 20:
            print('Not Weird')

    # Shorter Code:
    # print('Weird' if n%2==1 or (n%2==0 and n in range(6, 20+1)) else 'Not Weird' if n%2==0 and (n in range(2, 5+1) or n > 20) else None)