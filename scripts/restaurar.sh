#!/bin/bash

# Nombre del contenedor
CONTAINER="mysql-devops"
# Usuario y contraseña de MySQL
USER="root"
PASSWORD="rootpass"
# Nombre de la base de datos
DATABASE="devops_db"
# Ruta al archivo de respaldo
BACKUP_FILE="respaldo/backup_devops_db_2025-05-06_10-20-37.sql"  # Puedes actualizar la fecha si usas otro archivo

echo "♻️ Restaurando base de datos desde: $BACKUP_FILE"

# Verificar si el archivo existe
if [ ! -f "$BACKUP_FILE" ]; then
  echo "❌ El archivo de respaldo no existe: $BACKUP_FILE"
  exit 1
fi

# Restaurar usando docker exec
docker exec -i $CONTAINER mysql -u$USER -p$PASSWORD $DATABASE < "$BACKUP_FILE"

if [ $? -eq 0 ]; then
  echo "✅ Restauración completada exitosamente."
else
  echo "❌ Error durante la restauración."
fi
