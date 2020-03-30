# Written: 07-Jan-2020
# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count+=1
    return count

    # return len([i for i in range(len(string)) if string[i:].startswith(sub_string)])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
