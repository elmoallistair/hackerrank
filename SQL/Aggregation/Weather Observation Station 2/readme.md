[comment]: <> (Written: 01-Apr-2020)

## Weather Observation Station 2
Query the following two values from the **STATION** table:
1. The sum of all values in LAT_N rounded to a scale of 2 decimal places.
2. The sum of all values in LONG_W rounded to a scale of 2 decimal places.

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

### Output Format

Your results must be in the form:
```
lat lon
```
where **_lat_** is the sum of all values in LAT_N and **_lon_** is the sum of all values in LONG_W. 
Both results must be rounded to a scale of 2 decimal places.


&nbsp;
## Solution (MySQL)
```
SELECT 
  ROUND(SUM(lat_n), 2) AS lat,
  ROUND(SUM(long_w), 2) AS lon
FROM station;
```
