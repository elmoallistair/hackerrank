SELECT
    country.continent,
    FLOOR(AVG(city.population))
FROM
    city, country
WHERE 
    city.countrycode = country.code
GROUP BY
    country.continent
