-- Written: 01-Apr-2020

SELECT ROUND(MIN(lat_n), 4)
FROM station
WHERE lat_n > 38.7780;