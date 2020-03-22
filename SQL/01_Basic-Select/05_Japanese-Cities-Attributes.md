[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
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
> SELECT * FROM City WHERE countrycode='JPN';
