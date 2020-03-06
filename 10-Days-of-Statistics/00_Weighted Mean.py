# Written: 16-Jan-2020
'''
* Resource: https://www.hackerrank.com/challenges/s10-weighted-mean/tutorial
*
* Task:
*   Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements.
*   Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

# The first line contains an integer, N, denoting the number of elements in arrays X and W.
N = int(input())    # 5 <= N <= 50
# The second line contains N space-separated integers describing the respective elements of array X.
X = list(map(int, input().split()))     # 0 < xi <= 100, where xi is the i-th element of array X.
# The third line contains N space-separated integers describing the respective elements of array W.
W = list(map(int, input().split()))     # 0 < wi <= 100, where wi is the i-th element of array W.

xiwi = wi = 0
for i in range(N):
    xiwi += (X[i] * W[i])
    wi += W[i]

Mw = xiwi/wi
# Your answer should be rounded to a scale of 1 decimal place
print(round(Mw, 1))

# Shorter Code:
# print(round(sum([X[i]*W[i] for i in range(N)]) / sum([W[i] for i in range(N)]),1))
