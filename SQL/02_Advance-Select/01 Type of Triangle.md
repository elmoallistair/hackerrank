[comment]: <> (Written: 25-Mar-2002)

# Type of Triangle
Write a query identifying the type of each record in the <b>TRIANGLES</b> table using its three side lengths. 
Output one of the following statements for each record in the table:
* <b>Equilateral</b>: It's a triangle with <b>3</b> sides of equal length.
* <b>Isosceles</b>: It's a triangle with <b>2</b> sides of equal length.
* <b>Scalene</b>: It's a triangle with <b>3</b> Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:
* <b>Equilateral</b>: It's a triangle with  sides of equal length.

## Input Format
The <b>TRIANGLES</b> table is described as follows:
| Column | Type    |
|--------|---------|
| A      | Integer |
| B      | Integer |
| C      | Integer |

Each row in the table denotes the lengths of each of a triangle's three sides.

## Sample Input
| A  | B  | C  |
|----|----|----|
| 20 | 20 | 23 |
| 20 | 20 | 20 |
| 20 | 21 | 22 |
| 13 | 14 | 30 |

## Sample Output
```
Isosceles
Equilateral
Scalene
Not A Triangle
```

## Explanation
Values in the tuple <b>(20,20,23)</b> form an Isosceles triangle, because <b><i>A &#8801; B</i></b>.<br>
Values in the tuple <b>(20,20,20)</b> form an Equilateral triangle, because <b><i>A &#8801; B &#8801; C</i></b>. Values in the tuple <b>(20,21,22)</b> form a Scalene triangle, because <b><i>A &#8802; B &#8802; C</i></b>.<br>
Values in the tuple <b>(13,14,30)</b> cannot form a triangle because the combined value of sides <b><i>A</i></b> and <b><i>B</i></b> is not larger than that of side <b><i>C</i></b>.

## Solution (MySQL)
```
SELECT
  CASE
    WHEN (A + B <= C) OR (B + C <= A) OR (C + A <= B) THEN "Not A Triangle"
    WHEN (A = B AND B = C) THEN "Equilateral"
    WHEN (A = B AND B <> C) OR (B = C AND C <> A) OR (C = A AND A <> B) THEN "Isosceles"
  ELSE "Scalene"
END
FROM triangles;
```
    

