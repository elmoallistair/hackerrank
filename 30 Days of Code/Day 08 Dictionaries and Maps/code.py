# Written: 11-Jan-2020
# https://www.hackerrank.com/challenges/30-dictionaries-and-maps

# Enter your code here. Read input from STDIN. Print output to STDOUT
phoneBook = dict()
n = int(input())

for i in range(n):
    query = list(input().split())
    phoneBook.update({query[0]:query[1]})

for i in range(n):
    name = input()
    try:
        print("{}={}".format(name, phoneBook[name]))
    except:
        print("Not found")

