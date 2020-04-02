-- Written: 01-Apr-2020
SET @doc=0, @prof =0, @sing=0, @act=0;

SELECT 
  MIN(Doctor), 
  MIN(Professor), 
  MIN(Singer), 
  MIN(Actor) 
FROM (
  SELECT 
    CASE Occupation 
      WHEN 'Doctor' THEN @doc:=@doc+1
      WHEN 'Professor' THEN @prof:=@prof+1
      WHEN 'Singer' THEN @sing:=@sing+1
      WHEN 'Actor' THEN @act:=@act+1 
    END AS row,
    CASE WHEN occupation = 'Doctor' THEN name END AS Doctor,
    CASE WHEN occupation = 'Professor' THEN name END AS Professor,
    CASE WHEN occupation = 'Singer' THEN name END AS Singer,
    CASE WHEN occupation = 'Actor' THEN name END AS Actor
  FROM OCCUPATIONS ORDER BY Name
) AS new_table
GROUP BY row;