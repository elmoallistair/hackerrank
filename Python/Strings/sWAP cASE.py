# Written: 17-Jan-2020
# https://www.hackerrank.com/challenges/swap-case/problem

def swap_case(s):
    return ''.join([i.lower() if i.isupper() else i.upper() for i in S])
    # return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
