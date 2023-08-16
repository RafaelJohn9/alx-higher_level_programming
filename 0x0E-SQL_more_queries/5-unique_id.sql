-- a script that creates the table unique_id on your MYSQL server
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
