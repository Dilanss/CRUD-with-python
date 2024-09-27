CREATE DATABASE CRUD;
USE CRUD;

CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    cantidad int NOT NULL,
    precio DECIMAL(10, 2)
    descripcion TEXT
);
