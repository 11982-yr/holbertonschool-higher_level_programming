-- 17. Go to UTF8
-- Converts hbtn_0c_0 database, first_table and name field to utf8mb4 (utf8mb4_unicode_ci)

USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
