# Written: 07-Jan-2020
# https://www.hackerrank.com/challenges/python-tuples/problem

def solution(n):
    t = tuple(n)
    print(hash(t))

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    solution(integer_list)