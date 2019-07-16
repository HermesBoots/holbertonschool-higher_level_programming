-- create a new user with full privileges on this server
-- create user
CREATE USER IF NOT EXISTS user_0d_1@localhost
IDENTIFIED BY 'user_0d_1_pwd';
-- grant privileges
GRANT ALL ON *.* TO user_0d_1@localhost;
