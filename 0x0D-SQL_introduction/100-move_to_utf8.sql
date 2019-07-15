-- convert a database to the UTF-8 character set and collation

-- change the database defaults
ALTER DATABASE CHARACTER SET utf8mb4;
ALTER DATABASE COLLATE utf8mb4_unicode_ci;

-- change the table default
ALTER TABLE first_table CHARACTER SET utf8mb4;
ALTER TABLE first_table COLLATE utf8mb4_unicode_ci;

-- convert the existing string column
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
