# Written: 07-Jan-2020
# https://www.hackerrank.com/challenges/python-lists/problem

def solution(N):
    for _ in range(N):
        cmd = input().split()
        func = cmd[0]

        if func == 'insert': 
            arr.insert(int(cmd[1]), int(cmd[2]))
        elif func == 'print': 
            print(arr)
        elif func == 'remove': 
            arr.remove(int(cmd[1]))
        elif func == 'append': 
            arr.append(int(cmd[1]))
        elif func == 'sort': 
            arr.sort()
        elif func == 'pop': 
            arr.pop()
        elif func == 'reverse': 
            arr.reverse()

if __name__ == '__main__':
    arr = list()
    N = int(input())
    
    solution(N)