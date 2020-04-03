# Written: 02-Apr-2020
# https://www.hackerrank.com/challenges/symmetric-difference/problem

_ = int(input())
M = set(list(map(int, input().split())))

_ = int(input())
N = set(list(map(int, input().split())))

res = M.symmetric_difference(N)
# res = M ^ N

for i in sorted(res):
    print(i)
