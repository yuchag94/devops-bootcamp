#!/bin/bash

echo "📥 ¿Cuál es tu nombre?"
read nombre

echo "📡 Esperando a que MySQL acepte conexiones..."

# Espera real hasta que MySQL esté activo y aceptando comandos
until mysqladmin ping -h mysql-devops -u root -prootpass --silent; do
  echo "⏳ MySQL aún no responde, esperando..."
  sleep 2
done

echo "✅ Conectado a MySQL"

# Ejecutar comandos
mysql -h mysql-devops -u root -prootpass devops_db <<EOF
CREATE TABLE IF NOT EXISTS alumnos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  fecha_ingreso DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO alumnos (nombre) VALUES ('$nombre');

SELECT * FROM alumnos;
EOF

echo "🏁 Nombre guardado exitosamente: $nombre"
