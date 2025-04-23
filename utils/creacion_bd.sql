-- CREATE DATABASE automated_marketing;
-- USE DATABASE automated_marketing;

CREATE TABLE usuario_roles(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre_rol TEXT UNIQUE NOT null
);

CREATE TABLE usuario(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre_usuario TEXT UNIQUE NOT null,
	correo TEXT UNIQUE NOT NULL,
	contrasena TEXT NOT NULL,
	rol_id INT NOT NULL,
	FOREIGN KEY (rol_id) REFERENCES usuario_roles(id)
);

CREATE TABLE campania(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre TEXT NOT NULL,
	descripcion TEXT,
	fecha_inicio DATETIME NOT NULL,
	fecha_fin DATETIME
);

CREATE TABLE campania_detalles(
	id INT PRIMARY KEY AUTO_INCREMENT,
	campania_id INT NOT NULL,
	item TEXT,
	cliente_id INT NOT NULL,
	FOREIGN KEY (campania_id) REFERENCES campania(id)
);

CREATE TABLE cliente(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre TEXT NOT NULL,
	apellido TEXT NOT NULL,
	telefeno VARCHAR(10),
	usuario_id INT UNIQUE,
	FOREIGN KEY (usuario_id) REFERENCES usuario(id)
);

CREATE TABLE planificador(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	campania_id INT NOT NULL,
	estatus ENUM('enviado', 'pendiente', 'error') NOT NULL,
	fecha_creacion TIMESTAMP,
	FOREIGN KEY (campania_id) REFERENCES campania(id),
	FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE metrica(
	id INT PRIMARY KEY AUTO_INCREMENT,
	nombre TEXT,
	descripcion TEXT,
	fecha_creacion TIMESTAMP,
	fecha_actualizacion TIMESTAMP
);

CREATE TABLE reporte(
	id INT PRIMARY KEY AUTO_INCREMENT,
	cliente_id INT NOT NULL,
	metrica_id INT NOT NULL,
	descripcion TEXT,
	fecha_creacion TIMESTAMP,
	FOREIGN KEY (cliente_id) REFERENCES cliente(id),
	FOREIGN KEY (metrica_id) REFERENCES metrica(id)
);

CREATE TABLE log_tableau(
	id INT PRIMARY KEY AUTO_INCREMENT,
	estatus TEXT,
	descripcion TEXT,
	fecha_creacion TIMESTAMP
);
