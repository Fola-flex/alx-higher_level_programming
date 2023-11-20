-- Lists all cities in database hbtn_0d_usa
-- should display cities.id - cities.name - states.name
-- results should be sorted in asceding order by cities.id

SELECT cities.id, cities.name, states.name 
  FROM cities LEFT JOIN states ON states.id = cities.state_id 
ORDER BY cities.id ASC;
