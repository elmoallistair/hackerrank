[comment]: <> (Written: 23-Mar-2020)

<b>TASK<b>
> Query all columns for all American cities in CITY with populations larger than 100000. The CountryCode for America is USA. 
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
> SELECT * FROM city WHERE countrycode = 'USA' AND population > 100000;
