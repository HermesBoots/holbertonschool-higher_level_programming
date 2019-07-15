-- convert a database to the UTF-8 character set and collation

-- change the database defaults
ALTER DATABASE CHARACTER SET utf8mb4;
ALTER DATABASE COLLATE utf8mb4_unicode_ci;

-- change the table default
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
