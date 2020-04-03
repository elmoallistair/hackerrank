# Written: 03-Apr-2020
# https://www.hackerrank.com/challenges/python-mod-divmod/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
	a = int(input())
	b = int(input())

	print(int(a//b))
	print(a%b)
	print(divmod(a,b))
