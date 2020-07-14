-- Create database with a table.
-- USING KEY AND FOREIGN KEY
CREATE DATABASE IF NOT exists hbtn_0d_usa;
CREATE TABLE IF NOT exists hbtn_0d_usa.cities (
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
state_id INT FOREIGN KEY REFERENCES hbtn_0d_usa.states(id) NOT NULL,
name VARCHAR(256) NOT NULL);
