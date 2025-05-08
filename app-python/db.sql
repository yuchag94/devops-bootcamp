CREATE TABLE IF NOT EXISTS vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarjeta_propiedad VARCHAR(50),
    soat VARCHAR(50),
    poliza VARCHAR(50),
    revision DATE,
    gps VARCHAR(50),
    clave_gps VARCHAR(50)
);