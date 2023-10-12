-- SQL create a users table with three columns
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY AUTO_INCREMENT INDEX,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
);
