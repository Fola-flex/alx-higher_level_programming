-- Displays the max temperature of each state
SELECT state, MAX(value) A max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
