-- script that creates a table called first_table in the current database
-- first_table description:
--     id INT
--     name VARCHAR(256)
-- database name will be passed as an argument of the mysql command
-- If the table first_table already exists, your script should not fail
-- You are not allowed to use the SELECT or SHOW statements
CREATE TABLE IF NOT EXISTS first_table (`id` INT, `name` VARCHAR(256));
