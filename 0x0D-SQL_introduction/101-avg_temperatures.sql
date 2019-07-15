-- find the average temperatures in each city and display them in order
SELECT city, avg(value) AS avg_temp FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
