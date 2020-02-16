# Written: 14-Jan-2020
'''
* Resources: https://www.hackerrank.com/challenges/30-2d-arrays/tutorial
*
* Context:
*   Given a 6x6 2D Array, A:
*     1 1 1 0 0 0
*     0 1 0 0 0 0
*     1 1 1 0 0 0
*     0 0 0 0 0 0
*     0 0 0 0 0 0
*     0 0 0 0 0 0
*
*   We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
*     a b c
*       d
*     e f g
*
*   There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
*
* Task:
*   Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
*
* Input Format
*   There are 6 lines of input, where each line contains 6 space-separated integers describing 2D Array A;
*   every value in A will be in the inclusive range of -9 to 9.
*
* Constraints
*   - -9 <= A[i][j] <= 9
*   - 0 <= i,j <= 5
*
* Output Format
*   Print the largest (maximum) hourglass sum found in A.
*
* Sample Input
*   1 1 1 0 0 0
*   0 1 0 0 0 0
*   1 1 1 0 0 0
*   0 0 2 4 4 0
*   0 0 0 2 0 0
*   0 0 1 2 4 0
*
* Sample Output
*   19
*
* Explanation
*   A contains the following hourglasses:
*
*    1 1 1   1 1 0   1 0 0   0 0 0
*      1       0       0       0
*    1 1 1   1 1 0   1 0 0   0 0 0
*
*    0 1 0   1 0 0   0 0 0   0 0 0
*      1       1       0       0
*    0 0 2   0 2 4   2 4 4   4 4 0
*
*    1 1 1   1 1 0   1 0 0   0 0 0
*      0       2       4       4
*    0 0 0   0 0 2   0 2 0   2 0 0
*
*    0 0 2   0 2 4   2 4 4   4 4 0
*      0       0       2       0
*    0 0 1   0 1 2   1 2 4   2 4 0
*
*   The hourglass with the maximum sum (19) is:
*    2 4 4
*      2
*    1 2 4
'''

# ===============================================

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []
    arrsum = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for row in range(len(arr) - 2):
        for col in range(len(arr[row]) - 2):
            a = int(arr[row][col])
            b = int(arr[row][col+1])
            c = int(arr[row][col+2])
            d = int(arr[row+1][col+1])
            e = int(arr[row+2][col])
            f = int(arr[row+2][col+1])
            g = int(arr[row+2][col+2])
            sum = a + b + c + d + e + f + g
            arrsum.append(sum)
    print(arrsum)
    print(max(arrsum))