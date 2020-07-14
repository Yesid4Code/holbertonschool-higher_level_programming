-- Create a database and a table inside.
-- with unique and key
CREATE DATABASE if not exists hbtn_0d_usa;
CREATE TABLE if not exists hbtn_0d_usa.states (
id INT not NULL AUTO_INCREMENT UNIQUE,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id));
