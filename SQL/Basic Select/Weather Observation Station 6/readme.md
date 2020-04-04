[comment]: <> (Written: 23-Mar-2020)

## Weather Observation Station 6
Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from **STATION**. 
Your result cannot contain duplicates.

### Input Format
The **STATION** table is described as follows:
 
| Field  | Type         |
|--------|--------------|
| ID     | NUMBER       |
| CITY   | VARCHAR2(21) |
| STATE  | VARCHAR2(2)  |
| LAN_N  | NUMBER       |
| LONG_W | NUMBER       |

where LAT_N is the northern latitude and LONG_W is the western longitude.

&nbsp;
## Solution (MySQL)
```
SELECT DISTINCT(city) 
FROM station 
WHERE city REGEXP '^[aeiou]';
```
[Reference](https://www.tutorialspoint.com/mysql/mysql-regexps.htm)
