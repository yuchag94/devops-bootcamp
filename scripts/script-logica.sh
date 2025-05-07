#!/bin/bash

echo "📘 ¿Cuál es tu nombre?"
read nombre

echo "📡 Esperando a que MySQL acepte conexiones..."

# Esperar hasta que MySQL esté listo
until mysqladmin ping -h db -u root -prootpass --silent; do
  echo "⌛ MySQL aún no responde, esperando..."
  sleep 2
done

echo "✅ Conectado a MySQL"

# Ejecutar el INSERT
fecha=$(date '+%F %T')
mysql -h db -u root -prootpass devops_db -e "INSERT INTO alumnos (nombre, fecha_ingreso) VALUES ('$nombre', '$fecha');"

echo "🏁 Nombre guardado exitosamente: $nombre"
