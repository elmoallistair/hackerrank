-- Written: 23-Mar-2020

SELECT DISTINCT(city) 
FROM station 
WHERE city REGEXP '[^aeiou]$';