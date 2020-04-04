[comment]: <> (Written: 02-Apr-2020)

## Weather Observation Station 19
Consider **_P<sub>1</sub>(a,c)_** and **_P<sub>2</sub>(b,d)_** to be two points on a 2D plane where **_(a,b)_** are the respective minimum and maximum values of Northern Latitude (LAT_N) and **_(c,d)_** are the respective minimum and maximum values of Western Longitude (LONG_W) in **STATION**.<br>

Query the Euclidean Distance between points **_P<sub>1</sub>_** and **_P<sub>2</sub>_** and format your answer to display 4 decimal digits.

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
SELECT ROUND(SQRT(
  POWER(MAX(lat_n)-MIN(lat_n),2) + 
  POWER(MAX(long_w)-MIN(long_w),2)
), 4)
FROM station;
```
