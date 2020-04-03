# Written: 03-Apr-2020
# https://www.hackerrank.com/challenges/find-angle/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    
    MBC = int(round(math.degrees(math.atan2(AB, BC))))
    print(str(MBC) + '°')
