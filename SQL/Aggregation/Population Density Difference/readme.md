[comment]: <> (Written: 01-Mar-2020)

## Population Density Difference
Query the difference between the maximum and minimum populations in **CITY**.

### Input Format
The **CITY** table is described as follows: 

| Field       | Type         |
|-------------|--------------|
| ID          | NUMBER       |
| NAME        | VARCHAR2(17) |
| COUNTRYCODE | VARCHAR2(3)  |
| DISTRICT    | VARCHAR2(20) |
| POPULATION  | NUMBER       |

&nbsp;
## Solution (MySQL)
```
SELECT MAX(population)-MIN(population) AS difference
FROM city;
```
