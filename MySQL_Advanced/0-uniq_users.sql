-- This script creates a 'users' table with the specified attributes.
-- The 'users' table includes the following columns:
-- - id: an integer that is never null, auto increments, is the primary key
-- - email: a string (255 characters), never null, and unique
-- - name: a string (255 characters)
-- If the table already exists, the script will not fail.


DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY (id)
);
