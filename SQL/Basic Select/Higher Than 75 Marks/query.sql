-- Written: 24-Mar-2020

SELECT Name 
FROM Students 
WHERE Marks>75 
ORDER BY RIGHT(Name, 3), ID;