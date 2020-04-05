-- Written: 23-Mar-2020

SELECT 
	city, 
	LENGTH(city) 
FROM station 
ORDER BY LENGTH(city), city 
LIMIT 1;

SELECT 
	city, 
	LENGTH(city) 
FROM station 
ORDER BY LENGTH(city) DESC, city 
LIMIT 1;