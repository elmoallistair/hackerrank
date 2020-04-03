# Written: 03-Apr-2020
# https://www.hackerrank.com/challenges/polar-coordinates/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath

if __name__ == '__main__':
    z = input()
    print(abs(complex(z)))
    print(cmath.phase(complex(z)))
