# Written: 07-Jan-2020
'''
* Task
*   You have a record of N students.
*   Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry.
*   The marks can be floating values. The user enters some integer followed by the names and marks for N students.
*   You are required to save the record in a dictionary data type. The user then enters a student's name.
*   Output the average percentage marks obtained by that student, correct to two decimal places.
*
* Input Format
*   The first line contains the integer N, the number of students.
*   The next N lines contains the name and marks obtained by that student separated by a space. The final line contains the name of a particular student previously listed.
*
* Constraints
*   2 <= N <= 10
*   0 <= Marks <= 100
*
* Output Format
*   Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
*
* Sample Input 0
*   3
*   Krishna 67 68 69
*   Arjun 70 98 63
*   Malika 52 56 60
*   Malika
*
* Sample Output 0
*   56.00
*
* Explanation 0
*   Marks for Malika are {52,56,60} whose average is 56
*
* Sample Input 1
*   2
*   Harsh 25 26.5 28
*   Anurag 26 28 30
*   Harsh
*
* Sample Output 1
*   26.50
'''

# ===============================================

if __name__ == '__main__':
    n = int(input())        # 2 <= N <= 10
    student_marks = {}      # 0 <= Marks <= 100
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    data = student_marks.get(query_name)    # get list of marks by query_name
    n = len(data)           # get marks length
    sum = 0
    for i in range(n):
        sum += data[i]
    ave = sum/n
    print("{0:.2f}".format(round(ave, 2)))  # output format: correct to 2 decimal places.
