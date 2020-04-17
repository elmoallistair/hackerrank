# Written: 16-Jan-2020
# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))

xiwi = wi = 0
for i in range(N):
    xiwi += (X[i] * W[i])
    wi += W[i]

Mw = xiwi/wi
# Your answer should be rounded to a scale of 1 decimal place
print(round(Mw, 1))

# print(round(sum([X[i]*W[i] for i in range(N)]) / sum([W[i] for i in range(N)]),1))
