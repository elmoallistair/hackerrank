# Written: 29-Mar-2020
# https://www.hackerrank.com/challenges/s10-quartiles/problem

def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) // 2

def quartiles(arr):
    n = len(arr)
    Q1 = median(arr[0:(n // 2)])
    Q2 = median(arr)
    if n % 2 == 1:
        Q3 = median(arr[(n // 2) + 1:])
    else:
        Q3 = median(arr[n // 2:])

    print("{}\n{}\n{}".format(Q1, Q2, Q3))


# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    X = list(map(int, input().split()))
    X = sorted(X)
    quartiles(X)
