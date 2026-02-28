-- Lists all cities in hbtn_0d_usa with their respective state names
-- Displays: cities.id - cities.name - states.name
-- Sorted by cities.id in ascending order
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states ON cities.state_id = states.id 
ORDER BY cities.id ASC;
