SELECT
    w.id,
    wp.age,
    w.coins_needed,
    w.power
FROM
    wands w JOIN wands_property wp ON w.code = wp.code 
WHERE
    is_evil = 0 AND
    coins_needed = (SELECT MIN(coins_needed)
                    FROM wands x JOIN wands_property y ON x.code = y.code
                    WHERE x.power = w.power AND y.age = wp.age)
ORDER BY
    w.power DESC, wp.age DESC