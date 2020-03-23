[comment]: <> (Written: 24-Mar-2020)

<b>TASK</b>
> Query the Name of any student in STUDENTS who scored higher than _75_ Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

<b>Input Format</b>
> The STUDENTS table is described as follows: 
> | Column | Type    |
> |--------|---------|
> | ID     | Integer |
> | Name   | String  |
> | Marks  | Integer |
> 
> The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.

<b>Sample Input</b>
> | ID | Name     | Marks |
> |----|----------|-------|
> | 1  | Ashley   | 81    |
> | 2  | Samantha | 75    |
> | 4  | Julia    | 76    |
> | 3  | Belvet   | 84    |

<b>Sample Output</b>
> Ashle <br>
> Julia <br>
> Belvet <br>

<b>Explanation</b>
> Only Ashley, Julia, and Belvet have Marks > _75_. If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'. 

<br><br>
<b>ANSWER (MySQL)</b>
> SELECT Name FROM Students WHERE Marks>75 ORDER BY RIGHT(Name, 3), ID;
