-- display the top 3 of the cities temperature during July..
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month >=7 AND month <9
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;
