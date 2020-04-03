# Written: 08-Jan-2020
# https://www.hackerrank.com/challenges/text-wrap/problem

import textwrap as tw

def wrap(string, max_width):
    return "\n".join(textwrap.TextWrapper(width=max_width).wrap(text=string))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    max_width = 4
    result = wrap(string, max_width)
    print(result)
