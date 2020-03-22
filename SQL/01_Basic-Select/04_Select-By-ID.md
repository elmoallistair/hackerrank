[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Query all columns for a city in CITY with the ID 1661.
>
> City Table: 
> | Field       | Type         |
> |-------------|--------------|
> | ID          | NUMBER       |
> | NAME        | VARCHAR2(17) |
> | COUNTRYCODE | VARCHAR2(3)  |
> | DISTRICT    | VARCHAR2(20) |
> | POPULATION  | NUMBER       |

<b>SOLUTION</b>
> SELECT * FROM City WHERE ID=1661;
