# Written: 07-Jan-2020
'''
* Task
*   Consider a list (list = []). You can perform the following commands:
*   1. insert i e: Insert integer e at position i.
*   2. print: Print the list.
*   3. remove e: Delete the first occurrence of integer e.
*   4. append e: Insert integer e at the end of the list.
*   5. sort: Sort the list.
*   6. pop: Pop the last element from the list.
*   7. reverse: Reverse the list.
*   Initialize your list and read in the value of n followed by lines of commands where each command will be of the 7 types listed above.
*   Iterate through each command in order and perform the corresponding operation on your list.
*
* Input Format
*   The first line contains an integer, n, denoting the number of commands.
*   Each line i of the n subsequent lines contains one of the commands described above.
*
* Constraints
*   The elements added to the list must be integers.
*
* Output Format
*   For each command of type print, print the list on a new line.
*
* Sample Input 0
*   12
*   insert 0 5
*   insert 1 10
*   insert 0 6
*   print
*   remove 6
*   append 9
*   append 1
*   sort
*   print
*   pop
*   reverse
*   print
*
* Sample Output 0
*   [6, 5, 10]
*   [1, 5, 9, 10]
*   [9, 5, 1]
'''

# ===============================================

if __name__ == '__main__':
    arr = list()
    N = int(input())
    for i in range(N):
        cmd = input().split()
        func = cmd[0]

        if func == 'insert': arr.insert(int(cmd[1]), int(cmd[2]))
        elif func == 'print': print(arr)
        elif func == 'remove': arr.remove(int(cmd[1]))
        elif func == 'append': arr.append(int(cmd[1]))
        elif func == 'sort': arr.sort()
        elif func == 'pop': arr.pop()
        elif func == 'reverse': arr.reverse()