# Written: 23-Jan-2020
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

def solution(arr):
    arr = list(set(arr))
    arr.sort()
    print(arr[-2])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    solution(arr)