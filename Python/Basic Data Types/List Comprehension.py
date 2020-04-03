# Written: 23-Jan-2020
# https://www.hackerrank.com/challenges/list-comprehensions/problem


def solution(x,y,z,n):
    arr = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
    print(arr)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    solution(x,y,z,n)

    # Without comprehension
    # arr = []
    # for a in range(x+1):
    #     for b in range(y+1):
    #         for c in range(z+1):
    #             if a+b+c != n:
    #                 arr.append([a,b,c])
    # print(arr)