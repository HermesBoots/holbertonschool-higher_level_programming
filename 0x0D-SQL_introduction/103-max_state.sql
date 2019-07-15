-- show the maximum temperatures measured in each state, ordered alphabetically
SELECT state, max(value) AS max_temp FROM temperatures
GROUP BY state ORDER BY state;
