-- Written: 23-Mar-2020

SELECT (COUNT(city)-COUNT(DISTINCT(city))) 
FROM station;