-- a script that creates the MYSEL server used user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'MySQL' IDENTIFIED BY 'user_0d_1';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'MySQL';
