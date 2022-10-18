[comment]: <> (Written: 18-Oct-2022)

## Challenges
Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

### Input Format</b>

The following tables contain challenge data:

* **Hackers**: The hacker_id is the id of the hacker, and name is the name of the hacker. 

* **Challenges**: The challenge_id is the id of the challenge, and hacker_id is the id of the student who created the challenge.

&nbsp;
## Solution (MySQL)
```
SELECT
    h.hacker_id,
    h.name,
    COUNT(c.challenge_id) AS c_count
FROM 
    hackers h JOIN challenges c ON h.hacker_id = c.hacker_id
GROUP BY 
    h.hacker_id, h.name
HAVING
    c_count = (SELECT COUNT(c2.challenge_id) as c_max
               FROM challenges c2
               GROUP BY c2.hacker_id
               ORDER BY c_max DESC LIMIT 1)
    OR c_count IN (SELECT DISTINCT c_count2 AS c_unique
                   FROM (SELECT h2.hacker_id, COUNT(challenge_id) AS c_count2
                         FROM hackers h2 JOIN challenges c2
                         ON h2.hacker_id = c2.hacker_id
                         GROUP BY h2.hacker_id, h2.name) AS c_count3
                   GROUP BY c_count2
                   HAVING COUNT(c_count2) = 1)
ORDER BY 
    c_count DESC, h.hacker_id
```