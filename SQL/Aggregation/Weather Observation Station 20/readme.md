[comment]: <> (Written: 02-Apr-2020)

## Weather Observation Station 20
A median is defined as a number separating the higher half of a data set from the lower half. 
Query the median of the Northern Latitudes (LAT_N) from **STATION** and round your answer to 4 decimal places. 

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
## Solution (Oracle)
```
SELECT ROUND(MEDIAN(lat_n), 4)
FROM Station;
```
