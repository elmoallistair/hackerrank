[comment]: <> (Written: 01-Mar-2020)

## Average Population
Query the average population for all cities in **CITY**, rounded down to the nearest integer.

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
SELECT ROUND(AVG(Population))
FROM city;
```
