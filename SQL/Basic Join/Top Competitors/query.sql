SELECT 
    h.hacker_id,
    h.name
FROM
    hackers h INNER JOIN submissions s ON h.hacker_id = s.hacker_id
              INNER JOIN challenges c ON c.challenge_id = s.challenge_id
              INNER JOIN difficulty d ON d.difficulty_level = c.difficulty_level
WHERE
    s.score = d.score AND c.difficulty_level = d.difficulty_level
GROUP BY
    h.hacker_id, h.name
HAVING
    COUNT(s.hacker_id) > 1
ORDER BY
    COUNT(s.hacker_id) DESC, s.hacker_id