# Written: 29-Mar-2020
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2

def interquartile(arr):
    n = len(arr)
    Q1 = median(arr[0:(n // 2)])
    if n % 2 == 1:
        Q3 = median(arr[(n // 2) + 1:])
    else:
        Q3 = median(arr[n // 2:])
    print(float(Q3-Q1))

# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    frec = list(map(int, input().split()))
    dataset = [data[i] for i in range(len(data)) for j in range(frec[i])]
    dataset.sort()
    interquartile(dataset)
