-- Query para agregar la columna de 'provincia' a la tabla cliente.
USE automated_marketing;

ALTER TABLE cliente
ADD COLUMN provincia VARCHAR(23);

COMMIT;