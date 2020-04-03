# Written: 03-Apr-2020
# https://www.hackerrank.com/challenges/python-mod-divmod/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(input())
b = int(input())

print(int(a//b))
print(a%b)
print(divmod(a,b))
