# Written: 23-Jan-2020
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    return (sum([num for num in set(array)])/len(set(array)))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
