# Written: 04-Jan-2020
'''
* Resource: https://www.hackerrank.com/challenges/python-division/tutorial
*
* Task
*   Read two integers and print two lines.
*   The first line should contain integer division, a//b .
*   The second line should contain float division, a/b.
*   You don't need to perform any rounding or formatting operations.
*
* Input Format
*   The first line contains the first integer, a.
*   The second line contains the second integer, b.
*
* Output Format
*   Print the two lines as described above.
*
* Sample Input 0
*   4
*   3
*
* Sample Output 0
*   1
*   1.33333333333
'''

# ===============================================

if __name__ == '__main__':
    a = int(input())    # integer division
    b = int(input())    # float division

    print(a//b)
    print(a/b)