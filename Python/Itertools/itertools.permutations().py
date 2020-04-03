# Written: 22-Jan-2020
# https://www.hackerrank.com/challenges/itertools-permutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations
S = input().split()
for i in sorted(permutations(S[0], int(S[1]))):
    print (''.join(i))
