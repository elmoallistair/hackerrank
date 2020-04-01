-- Written: 01-Apr-2020

SELECT ROUND(
  ABS(MIN(lat_n)-MAX(lat_n)) + 
  ABS(MIN(long_w)-MAX(long_w))
  , 4)
FROM station;