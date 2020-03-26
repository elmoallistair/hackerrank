# Written: 01-Feb-2020
# https://www.hackerrank.com/challenges/30-sorting/problem

#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
def bubbleSort(list):
    count = 0
    for passnum in range(len(list)):
        for i in range(len(list)-passnum-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                count += 1
    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(list[0]))
    print("Last Element: {}".format(list[len(list)-1]))

bubbleSort(a)

