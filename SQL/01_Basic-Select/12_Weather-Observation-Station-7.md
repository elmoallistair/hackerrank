[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
>
> Station's Table: 
> | Field  | Type         |
> |--------|--------------|
> | ID     | NUMBER       |
> | CITY   | VARCHAR2(21) |
> | STATE  | VARCHAR2(2)  |
> | LAN_N  | NUMBER       |
> | LONG_W | NUMBER       |

<b>SOLUTION (MySQL)</b>
> SELECT DISTINCT(city) FROM station WHERE city REGEXP '[aeiou]$';<br><br>
> [Reference](https://www.tutorialspoint.com/mysql/mysql-regexps.htm)
