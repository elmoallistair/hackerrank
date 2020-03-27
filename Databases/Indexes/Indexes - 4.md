[comment]: <> (Written: 28-Mar-2020)

### Question
The correct syntax for creating composite indexes in MS SQL Sever is:
> * CREATE INDEX index_name ON table_name(column1), table_name(column2);
> * CREATE INDEX index_name ON table_name(column1) and table_name(column2);
> * CREATE INDEX index_name ON table_name(column1, column2);
> * All the above-mentioned syntax are correct.</p>

### Answer
> CREATE INDEX index_name ON table_name(column1, column2);

[Reference](https://www.mysqltutorial.org/mysql-index/mysql-composite-index/)
