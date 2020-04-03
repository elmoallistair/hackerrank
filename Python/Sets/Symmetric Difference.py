# Written: 02-Apr-2020
# https://www.hackerrank.com/challenges/symmetric-difference/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
	_ = int(input())
	M = set(list(map(int, input().split())))	

	_ = int(input())
	N = set(list(map(int, input().split())))	

	res = M.symmetric_difference(N)
	# res = M ^ N	

	for i in sorted(res):
	    print(i)