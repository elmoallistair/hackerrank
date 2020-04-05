-- Written: 01-Apr-2020

SELECT CEIL(AVG(salary)-AVG(REPLACE(salary,'0','')))
FROM employees;