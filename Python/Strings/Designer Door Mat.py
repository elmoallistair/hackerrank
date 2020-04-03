# Written: 08-Jan-2020
# https://www.hackerrank.com/challenges/designer-door-mat/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

for i in range(1, N, 2):
    print (('.|.' * i).center(M, '-'))  # Top side

print ('WELCOME'.center(M, '-'))        # Center

for i in range(N-2, -1, -2):
    print (('.|.' * i).center(M, '-'))  # Bottom side
