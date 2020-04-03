# Written: 06-Jan-2020
# https://www.hackerrank.com/challenges/nested-list/problem

def solution(students):
    scores = list(set([students[x][1] for x in range(len(students))]))
    scores.sort()
    sec_grade = scores[1]

    low_std = [std[0] for std in students if std[1] == sec_grade]
    low_std.sort()

    for i in low_std: 
        print(i)

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    solution(students)
