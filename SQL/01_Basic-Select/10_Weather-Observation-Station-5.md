[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
>
> Station's Table: 
> | Field  | Type         |
> |--------|--------------|
> | ID     | NUMBER       |
> | CITY   | VARCHAR2(21) |
> | STATE  | VARCHAR2(2)  |
> | LAN_N  | NUMBER       |
> | LONG_W | NUMBER       |

<b>Sample Input</b>
> Let's say that CITY only has four entries: DEF, ABC, PQRS and WXY

<b>Sample Output</b>
> ABC 3<br>
> PQRS 4

<b>Explanation</b>
> When ordered alphabetically, the CITY names are listed as ABC, DEF, PQRS, and WXY, with the respective lengths 3,3,4 and 3. 
The longest-named city is obviously PQRS, but there are 3 options for shortest-named city; we choose ABC, because it comes first alphabetically.

<b>Note</b>
> You can write two separate queries to get the desired output. It need not be a single query.

<b>SOLUTION (MySQL)</b>
> SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(city), city LIMIT 1; <br>
> SELECT city, LENGTH(city) FROM station ORDER BY LENGTH(ciry) DESC, city LIMIT 1;
