-- Create a table user with four columns id, email, name and country
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country enum('US', 'CO', 'TN') NOT NULL DEFAULT('US')
)