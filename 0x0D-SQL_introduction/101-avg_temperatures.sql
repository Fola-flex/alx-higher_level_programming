-- Displays the avg temperature (Fahrenheit) by city ordered by 
-- temperature in descending order
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city, avg_temp
ORDER BY avg_temp DESC
