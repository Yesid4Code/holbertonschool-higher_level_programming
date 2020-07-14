-- Display the max temperature or each state
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
