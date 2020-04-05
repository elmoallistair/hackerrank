-- Written: 23-Mar-2020

SELECT DISTINCT(city) 
FROM station 
WHERE MOD(ID, 2)=0;