CREATE DATABASE IF NOT EXISTS codigos_db;

USE codigos_db;

CREATE TABLE IF NOT EXISTS codigos_sequenciais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE,
    sec INT,
    Grupo CHAR(1),
    Tipo_Alimento CHAR(1),
    Pais CHAR(2)
);