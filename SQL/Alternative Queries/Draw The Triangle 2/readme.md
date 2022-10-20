[comment]: <> (Written: 20-Oct-2022)

## Draw The Triangle 1
P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

```
* 
* * 
* * * 
* * * * 
* * * * *
```

Write a query to print the pattern P(20).

&nbsp;
## Solution (MySQL)
```
SET @TEMP:=0; 
SELECT REPEAT("* ", @TEMP:= @TEMP + 1) 
FROM INFORMATION_SCHEMA.TABLES
LIMIT 20
```