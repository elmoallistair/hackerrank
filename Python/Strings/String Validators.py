# Written: 08-Jan-2020
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()

    print(any([x for x in s if x.isalnum()]))
    print(any([x for x in s if x.isalpha()]))
    print(any([x for x in s if x.isdigit()]))
    print(any([x for x in s if x.islower()]))
    print(any([x for x in s if x.isupper()]))