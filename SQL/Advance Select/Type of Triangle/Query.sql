SELECT
  CASE
    WHEN (A + B <= C) OR (B + C <= A) OR (C + A <= B) THEN "Not A Triangle"
    WHEN (A = B AND B = C) THEN "Equilateral"
    WHEN (A = B AND B <> C) OR (B = C AND C <> A) OR (C = A AND A <> B) THEN "Isosceles"
  ELSE "Scalene"
END
FROM triangles;
