[comment]: <> (Written: 31-Mar-2020)

## Revising Aggregations - The Count Function
Query a count of the number of cities in **CITY** having a Population larger than **100,000**.

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
SELECT COUNT(Population) 
FROM city 
WHERE population > 100000;
```
