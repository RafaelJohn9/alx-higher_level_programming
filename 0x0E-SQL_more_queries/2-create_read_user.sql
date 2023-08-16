-- creates the database hbtn_0d_2 if it does not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the user user_0d_2 if not exists
CREATE USER  IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grants the user user_0d_2 SELECT permission
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
