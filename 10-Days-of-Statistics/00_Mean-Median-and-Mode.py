# Written: 15-Jan-2020
'''
* Resource: https://www.hackerrank.com/challenges/s10-basic-statistics/tutorial
*
* Task:
*   Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines.
*   If your array contains more than one modal value, choose the numerically smallest one.
*
* Note:
*   Other than the modal value (which will always be an integer),
*   your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).
'''


# Enter your code here. Read input from STDIN. Print output to STDOUT
# The first line contains an integer, N, denoting the number of elements in the array.
N = int(input())    # 10 <= N <= 2500
# The second line contains N space-separated integers describing the array's elements.
arr = list(map(int, input().split()))     # 0 < xi <= 10**5, where xi is the i-th element of the array

# Print 3 lines of output in the following order:
# 1. Print the mean on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
sum = 0
for i in arr:
    sum += i    # get sum of arr
mean = sum/N
print(mean)

# 2. Print the median on a new line, to a scale of 1 decimal place (i.e., 12.3, 7.0).
new_arr = sorted(arr)      # sort array
if len(new_arr) % 2 == 0:      # arr length is even?
    median = (new_arr[len(new_arr)//2] + new_arr[len(new_arr)//2 - 1])/2
elif len(new_arr) % 2 != 0:    # arr length is odd?
    median = new_arr[len(new_arr)//2]
print(median)

# 3. Print the mode on a new line; if more than one such value exists, print the numerically smallest one.for i in copy:
# -- UPDATE LATER --


# Shorter Code:
# import numpy as np
# from scipy import stats
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# print(np.mean(arr))
# print(np.median(arr))
# print(int(stats.mode(arr)[0]))
