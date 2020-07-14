-- Create database with a table using key and foreign key
CREATE DATABASE IF NOT exists hbtn_0d_usa;
CREATE TABLE IF NOT exists hbtn_0d_usa.cities (
id INT PRIMARY KEY NOT NULL,
state_id INT FOREIGN KEY REFERENCES hbtn_0d_usa(id) NOT NULL,
name VARCHAR(256) NOT NULL);
