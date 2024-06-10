-- Create a table to store users with their email, name, and country
-- The email is unique and not null, the name is optional
-- The country is an ENUM with three possible values, default to 'US' if not provided


CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US','CO','TN') NOT NULL DEFAULT 'US'
);
