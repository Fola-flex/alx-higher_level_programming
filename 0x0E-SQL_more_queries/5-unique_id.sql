-- Creates the table unique_id with:
--  id INT with default value 1 nad must be unique
--  name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256)) 
