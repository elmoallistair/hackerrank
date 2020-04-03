# Written: 27-Jan-2020
# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    n = len(string)
    splitNum = n/k;
    for i in range(0, n, k):
        str = string[i:i+k];
        sub = ''
        for s in str:
            if s not in sub:
                sub += s;
        print(sub)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)