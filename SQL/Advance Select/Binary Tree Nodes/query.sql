-- Written: 01-Apr-2020

SELECT 
  N, 
  CASE 
   WHEN P IS NULL THEN 'Root' 
   WHEN(
     SELECT COUNT(*) 
     FROM bst 
     WHERE P = x.N
   ) > 0 THEN 'Inner' ELSE 'Leaf'
  END
FROM bst x
ORDER BY N;

New Company
SELECT 
  company_code, 
  founder,
  (SELECT COUNT(DISTINCT lead_manager_code) FROM lead_manager WHERE company_code = c.company_code),
  (SELECT COUNT(DISTINCT senior_manager_code) FROM senior_manager WHERE company_code = c.company_code),
  (SELECT COUNT(DISTINCT manager_code) FROM manager WHERE company_code = c.company_code),
  (SELECT COUNT(DISTINCT employee_code) FROM employee WHERE company_code = c.company_code)
FROM company c
ORDER BY company_code;