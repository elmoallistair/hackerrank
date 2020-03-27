# Written: 02-Jan-2020
# https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # Grading policy:
    # Every student receives a in the inclusive range from 0 to 100.
    # Any grade less than 40 is a failing grade.
    new_grades = []

    for i in grades:
        div = i // 5  # Floor div of i
        mult = 5 * div  # Multiple of 5
        next_mult = 5 * (div + 1)  # Next multiple of 5
        diff = next_mult - i  # Difference between the grade and the next multiple of 5
        # If the difference between the grade and the next multiple of 5 is less than 3, round up to the next multiple of 5.
        # If the value of is less than 38, no rounding occurs as the result will still be a failing grade.
        if i >= 38 and diff < 3:
            new_grades.append(next_mult)
        else:
            new_grades.append(i)
    return new_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
