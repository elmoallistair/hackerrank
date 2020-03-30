# Written: 08-Jan-2020
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()

    # In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
    print(any([x for x in s if x.isalnum()]))
    # In the second line, print True if S has any alphabetical characters. Otherwise, print False.
    print(any([x for x in s if x.isalpha()]))
    # In the third line, print True if S has any digits. Otherwise, print False.
    print(any([x for x in s if x.isdigit()]))
    # In the fourth line, print True if S Has any lowercase characters. Otherwise, print False.
    print(any([x for x in s if x.islower()]))
    # In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
    print(any([x for x in s if x.isupper()]))
