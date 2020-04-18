# Written: 16-Jan-2020
# https://www.hackerrank.com/challenges/s10-standard-deviation/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr = list(map(int, input().split()))
mean = sum(arr)/N

sqr_dis = 0
for i in arr:
    sqr_dis += (i - mean)**2

stdev = (sqr_dis/N)**0.5
print(round(stdev, 1))

# print(round((sum([(n-sum(arr)/N)**2 for n in arr])/N)**0.5, 1))
