[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Let _N_ be the number of CITY entries in STATION, and let be _N'_ the number of distinct CITY names in STATION; query the value of _N - N'_ from STATION. 
In other words, find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
>
> Station's Table: 
> | Field  | Type         |
> |--------|--------------|
> | ID     | NUMBER       |
> | CITY   | VARCHAR2(21) |
> | STATE  | VARCHAR2(2)  |
> | LAN_N  | NUMBER       |
> | LONG_W | NUMBER       |

<b>SOLUTION</b>
> SELECT (COUNT(city)-COUNT(DISTINCT(city))) FROM station;
