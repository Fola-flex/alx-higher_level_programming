-- Creates server user_0d_1 with all privileges
-- password should be set to user_0d_1_pwd
-- if user exists script shouldn't fail
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;
