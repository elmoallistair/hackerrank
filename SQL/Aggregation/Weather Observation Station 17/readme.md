[comment]: <> (Written: 02-Apr-2020)

## Weather Observation Station 13
Query the sum of Northern Latitudes (LAT_N) from **STATION** having values greater than **38.7880** and less than **137.2345**. 
Truncate your answer to 4 decimal places.

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
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;
```