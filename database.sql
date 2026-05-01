CREATE DATABASE IF NOT EXISTS lab03_flask
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE lab03_flask;

CREATE TABLE IF NOT EXISTS administradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    rol ENUM('admin', 'usuario') NOT NULL DEFAULT 'usuario'
);

INSERT INTO usuarios (nombre, email, rol) VALUES
('Juan Pérez', 'juan@example.com', 'usuario'),
('María López', 'maria@example.com', 'admin');