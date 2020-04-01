-- Written: 01-Apr-2020

SELECT ROUND(MAX(lat_n), 4)
FROM station
WHERE lat_n < 137.2345;