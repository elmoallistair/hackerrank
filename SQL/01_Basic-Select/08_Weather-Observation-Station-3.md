[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Query a list of CITY names from STATION with even ID numbers only. You may print the results in any order, but must exclude duplicates from your answer.
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
> SELECT DISTINCT(city) FROM station WHERE MOD(ID, 2)=0;
