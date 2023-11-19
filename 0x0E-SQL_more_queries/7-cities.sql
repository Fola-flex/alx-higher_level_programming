-- Creates databse hbtn_0d_usa and table cities
-- cities description:
--   id INT unique, auto generated, not null and is a primary key
--   state_id int, can't be null and must be a foreign key referencing id of states--   name varcar(256) can't be null.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY (states_id) REFERENCES states(id), name VARCHAR(256) NOT  NULL);
