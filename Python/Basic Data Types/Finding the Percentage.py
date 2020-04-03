# Written: 07-Jan-2020
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

import statistics

def solution():
    data = student_marks.get(query_name)
    avg = statistics.mean(data)
    print("{0:.2f}".format(round(avg, 2)))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    solution()