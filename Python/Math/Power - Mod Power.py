# Written: 03-Apr-2020
# https://www.hackerrank.com/challenges/python-power-mod-power/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
	a = int(input())
	b = int(input())
	m = int(input())

	print(pow(a,b))
	print(pow(a,b,m))