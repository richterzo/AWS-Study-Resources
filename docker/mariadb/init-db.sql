CREATE DATABASE IF NOT EXISTS mariaDB;
USE mariaDB;

CREATE TABLE IF NOT EXISTS clienti (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

INSERT INTO clienti (nome, email) VALUES ('Mario Rossi', 'mario.rossi@example.com');