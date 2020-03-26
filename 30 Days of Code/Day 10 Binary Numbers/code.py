# Written: 13-Jan-2020
# https://www.hackerrank.com/challenges/30-binary-numbers

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    binary = str(bin(n)[2:])
    arr = list()
    for i in range(len(binary)):
        count = 0
        if binary[i] == '1':
            count += 1
            for j in range(i+1, len(binary)):
                if binary[j] == '1':
                    count += 1
                else:
                    break
        arr.append(count)
    print(max(arr))