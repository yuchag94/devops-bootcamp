#!/bin/bash

echo "📦 Iniciando respaldo automático..."

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="backup_devops_db_${TIMESTAMP}.sql"
DESTINO="/respaldo/${BACKUP_FILE}"

mysqldump -h db -u root -prootpass devops_db > "$DESTINO"

if [ $? -eq 0 ]; then
  echo "✅ Respaldo guardado en: $DESTINO"
else
  echo "❌ Error al generar respaldo."
fi
