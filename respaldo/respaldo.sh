#!/bin/bash

mkdir -p respaldo

FECHA=$(date +%Y-%m-%d_%H-%M-%S)
ARCHIVO="respaldo/backup_devops_db_$FECHA.sql"

echo "📦 Generando respaldo en: $ARCHIVO"

docker exec mysql-devops mysqldump -uroot -prootpass devops_db > "$ARCHIVO"

if [ $? -eq 0 ]; then
  echo "✅ Respaldo exitoso!"
else
  echo "❌ Hubo un error al generar el respaldo."
fi
