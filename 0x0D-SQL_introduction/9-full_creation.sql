-- Creates a table second_table in database hbtn_0c_0
-- second_table description:
--  id - INT
--  name - VARCHAR(256)
--  score - INT
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
LOAD DATA LOCAL INFILE './students.txt' INTO TABLE second_table;
