-- Written: 24-Mar-2020

SELECT DISTINCT(city) 
FROM station 
WHERE city REGEXP '^[^aeiou].*[^aeiou]$';