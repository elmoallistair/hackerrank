[comment]: <> (Written: 02-Apr-2020)

## Weather Observation Station 18
Consider **_P<sub>1</sub>(a,b)_** and **_P<sub>2</sub>(a,b)_** to be two points on a 2D plane.
* **_a_** happens to equal the minimum value in Northern Latitude (LAT_N in **STATION**).
* **_b_** happens to equal the minimum value in Western Longitude (LONG_W in **STATION**).
* **_c_** happens to equal the maximum value in Northern Latitude (LAT_N in **STATION**).
* **_d_** happens to equal the maximum value in Western Longitude (LONG_W in **STATION**).

Query the Manhattan Distance between points  **_P<sub>1</sub>_** and  **_P<sub>2</sub>_** and round it to a scale of 4 decimal places.

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
SELECT ROUND(
  ABS(MIN(lat_n)-MAX(lat_n)) + 
  ABS(MIN(long_w)-MAX(long_w))
  , 4)
FROM station;
```