[comment]: <> (Written: 13-Oct-2022)

## Population Census
Given the **CITY** and **COUNTRY** tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

**Note**: CITY.CountryCode and COUNTRY.Code are matching key columns.

### Input Format</b>
The **CITY** and **COUNTRY** tables are described as follows: 

![city](city.jpg)
![country](country.jpg)

&nbsp;
## Solution (MySQL)
```
SELECT
    country.continent,
    FLOOR(AVG(city.population))
FROM
    city, country
WHERE 
    city.countrycode = country.code
GROUP BY
    country.continent
```