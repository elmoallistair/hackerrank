[comment]: <> (Written: 23-Mar-2020)

## Weather Observation Station 1
Query a list of CITY and STATE from the **STATION** table.

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
SELECT city, state 
FROM station;
```