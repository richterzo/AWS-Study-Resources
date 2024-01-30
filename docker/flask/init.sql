-- Use your desired database; make sure this matches with your Docker Compose setup
USE mydatabase;

-- Drop the table if it already exists and then create a new one
DROP TABLE IF EXISTS user;

-- Create the 'user' table
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    UNIQUE KEY unique_email (email)
);

-- Optional: Insert example data into the 'user' table
INSERT INTO user (username, password, email) VALUES ('user1', 'password1', 'user1@example.com');
INSERT INTO user (username, password, email) VALUES ('user2', 'password2', 'user2@example.com');
