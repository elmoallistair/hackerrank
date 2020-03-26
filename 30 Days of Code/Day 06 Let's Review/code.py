# Written: 09-Jan-2020
# https://www.hackerrank.com/challenges/30-review-loop

# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    S = input()
    arr1 = ''.join([S[x] for x in range(0, len(S), 2)])
    arr2 = ''.join([S[x] for x in range(1, len(S), 2)])
    print(arr1, arr2)

    # print(S[0::2], S[1::2])
