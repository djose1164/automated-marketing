
-- Inserciones para usuario_roles
INSERT INTO usuario_roles (nombre_rol) VALUES 
('Administrador'),
('Editor'),
('Cliente');

-- Inserciones para usuario
INSERT INTO usuario (nombre_usuario, correo, contrasena, rol_id) VALUES
('admin', 'admin@example.com', 'admin123', 1),
('editor_user', 'editor@example.com', 'editor123', 2),
('cliente_user', 'cliente@example.com', 'cliente123', 3),
('cliente_maria', 'maria@example.com', 'maria123', 3),
('cliente_jose', 'jose@example.com', 'jose123', 3);

-- Inserciones para cliente
INSERT INTO cliente (nombre, apellido, telefeno, usuario_id) VALUES
('Carlos', 'Pérez', '5551234567', 3),
('Maria', 'Lopez', '5557654321', 4),
('Jose', 'Martinez', '5558889999', 5);

-- Inserciones para campania
INSERT INTO campania (nombre, descripcion, fecha_inicio, fecha_fin) VALUES
('Campaña Primavera', 'Promoción de productos de primavera', '2025-04-01 00:00:00', '2025-05-31 23:59:59'),
('Campaña Verano', 'Promoción de verano', '2025-06-01 00:00:00', '2025-08-31 23:59:59');

-- Inserciones para campania_detalles
INSERT INTO campania_detalles (campania_id, item, cliente_id) VALUES
(1, 'Producto A', 1),
(1, 'Producto B', 2),
(2, 'Producto C', 3),
(2, 'Producto D', 1);

-- Inserciones para planificador
INSERT INTO planificador (cliente_id, campania_id, estatus, fecha_creacion) VALUES
(1, 1, 'pendiente', NOW()),
(2, 1, 'enviado', NOW()),
(3, 2, 'error', NOW()),
(1, 2, 'pendiente', NOW());

-- Inserciones para metrica
INSERT INTO metrica (nombre, descripcion, fecha_creacion, fecha_actualizacion) VALUES
('Visitas', 'Número de visitas al sitio web', NOW(), NOW()),
('Ventas', 'Número de ventas realizadas', NOW(), NOW()),
('Clicks', 'Número de clicks en anuncios', NOW(), NOW());

-- Inserciones para reporte
INSERT INTO reporte (cliente_id, metrica_id, descripcion, fecha_creacion) VALUES
(1, 1, 'Visitas en abril', NOW()),
(1, 2, 'Ventas en abril', NOW()),
(2, 1, 'Visitas en abril', NOW()),
(2, 3, 'Clicks en abril', NOW()),
(3, 2, 'Ventas en mayo', NOW());

-- Inserciones para log_tableau
INSERT INTO log_tableau (estatus, descripcion, fecha_creacion) VALUES
('Correcto', 'Carga de datos completada', NOW()),
('Error', 'Fallo en la conexión con Tableau', NOW()),
('Correcto', 'Sincronización exitosa', NOW()),
('Correcto', 'Exportación diaria realizada', NOW());
