# Written: 04-Jan-2020
'''
* Resource: https://www.hackerrank.com/challenges/python-arithmetic-operators/tutorial
*
* Task
* Read two integers from STDIN and print three lines where:
* - The first line contains the sum of the two numbers.
* - The second line contains the difference of the two numbers (first - second).
* - The third line contains the product of the two numbers.
*
* Input Format
*   The first line contains the first integer, a.
*   The second line contains the second integer, b.
*
* Constraints
*   1 <= a <= 10**10
*   1 <= b <= 10**10
*
* Output Format
*   Print the three lines as explained above.
*
* Sample Input 0
*   3
*   2
*
* Sample Output 0
*   5
*   1
*   6
*
* Explanation 0
*   3 + 2 => 5
*   3 - 2 => 1
*   3 * 2 => 6
'''

# ===============================================

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a+b)  # the sum of the two numbers.
    print(a-b)  # the difference of the two numbers.
    print(a*b)  # the product of the two numbers.
