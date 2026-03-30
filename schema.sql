CREATE DATABASE codigos_db;

USE codigos_db;

CREATE TABLE codigos_sequenciais (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10) UNIQUE,
    sec INT,
    Grupo CHAR(1),
    Tipo_Alimento CHAR(1),
    Pais CHAR(2)
);