# Written: 16-Jan-2020
'''
* Task:
*   Given an array, X, of N integers, calculate and print the standard deviation.
*   Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format).
*   An error margin of += 0.1 will be tolerated for the standard deviation.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
# The first line contains an integer, N, denoting the number of elements in the array.
N = int(input())    # 5 <= N <= 100
# The second line contains N space-separated integers describing the respective elements of the array.
arr = list(map(int, input().split()))   # 0 < xi <= 10**5, where xi is the i-th elment of array X.
# 1. Find the mean:
sum = 0
for i in arr:
    sum += i
mean = sum/N

# 2. Calculate the squared distance from the mean
sqr_dis = 0
for i in arr:
    sqr_dis += (i - mean)**2

# Round to a scale of 1 decimal place
stdev = (sqr_dis/N)**0.5
print(round(stdev, 1))

# Shorter Code:
# N = int(input())
# arr = list(map(int, input().split()))
# print(round((sum([(n-sum([n for n in arr])/N)**2 for n in arr])/N)**0.5, 1))
