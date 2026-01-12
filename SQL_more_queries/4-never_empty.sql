-- 4. ID can't be null
-- creates a table on MySQL server.

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
    );
