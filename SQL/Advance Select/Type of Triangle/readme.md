[comment]: <> (Written: 25-Mar-2020)

## Type of Triangle
Write a query identifying the type of each record in the **TRIANGLES** table using its three side lengths. 
Output one of the following statements for each record in the table:
* **Equilateral**: It's a triangle with **3** sides of equal length.
* **Isosceles**: It's a triangle with **2** sides of equal length.
* **Scalene**: It's a triangle with **3** Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:
* **Equilateral**: It's a triangle with  sides of equal length.

### Input Format
The **TRIANGLES** table is described as follows:

| Column | Type    |
|--------|---------|
| A      | Integer |
| B      | Integer |
| C      | Integer |

Each row in the table denotes the lengths of each of a triangle's three sides.

### Sample Input
| A  | B  | C  |
|----|----|----|
| 20 | 20 | 23 |
| 20 | 20 | 20 |
| 20 | 21 | 22 |
| 13 | 14 | 30 |

### Sample Output
```
Isosceles
Equilateral
Scalene
Not A Triangle
```

### Explanation
Values in the tuple **(20,20,23)** form an Isosceles triangle, because **_A &#8801; B_**.\
Values in the tuple **(20,20,20)** form an Equilateral triangle, because **_A &#8801; B &#8801; C_**.\
Values in the tuple **(20,21,22)** form a Scalene triangle, because **_A &#8802; B &#8802; C_**.\
Values in the tuple **(13,14,30)** cannot form a triangle because the combined value of sides **_A_** and **_B_** is not larger than that of side **_C_**.

&nbsp;
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