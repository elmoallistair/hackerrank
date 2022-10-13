[comment]: <> (Written: 13-Oct-2022)

## Population Census
Given the **CITY** and **COUNTRY** tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

**Note**: CITY.CountryCode and COUNTRY.Code are matching key columns.

### Input Format</b>
The **CITY** and **COUNTRY** tables are described as follows: 

![city](city.jpg)
![country](country.jpg)

&nbsp;
## Solution (MySQL)
```
SELECT
    SUM(city.population)
FROM
    city LEFT JOIN country ON city.countrycode = country.code
WHERE
    country.continent="Asia"
```