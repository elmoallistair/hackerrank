-- Written: 01-Apr-2020

SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;