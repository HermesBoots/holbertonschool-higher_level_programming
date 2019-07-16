-- create a database and a table to store U.S. cities
-- create the database
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- switch to the database
USE `hbtn_0d_usa`;
-- create the table
CREATE TABLE IF NOT EXISTS `cities` (
	`id` INT PRIMARY KEY AUTO_INCREMENT,
	`state_id` INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);
