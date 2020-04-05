[comment]: <> (Written: 23-Mar-2020)

## Weather Observation Station 3
Query a list of CITY names from STATION with even ID numbers only. You may print the results in any order, but must exclude duplicates from your answer.

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
WHERE MOD(ID, 2)=0;
```