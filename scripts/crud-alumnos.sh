#!/bin/bash

echo "🔨 Creando tabla 'alumnos'..."
docker exec -it mysql-devops mysql -uroot -prootpass -e "
USE devops_db;
CREATE TABLE IF NOT EXISTS alumnos (
  id INT PRIMARY KEY,
  nombre VARCHAR(50)
);
"

echo "📝 Insertando registros..."
docker exec -it mysql-devops mysql -uroot -prootpass -e "
USE devops_db;
INSERT INTO alumnos (id, nombre) VALUES
  (1, 'Yuliet'),
  (2, 'Juan'),
  (3, 'Ana');
"

echo "📖 Mostrando registros..."
docker exec -it mysql-devops mysql -uroot -prootpass -e "
USE devops_db;
SELECT * FROM alumnos;
"

echo "🔄 Actualizando registro con id=1..."
docker exec -it mysql-devops mysql -uroot -prootpass -e "
USE devops_db;
UPDATE alumnos SET nombre = 'Julieta' WHERE id = 1;
"

echo "🗑️ Eliminando registro con id=2..."
docker exec -it mysql-devops mysql -uroot -prootpass -e "
USE devops_db;
DELETE FROM alumnos WHERE id = 2;
"

echo "✅ Resultado final:"
docker exec -it mysql-devops mysql -uroot -prootpass -e "
USE devops_db;
SELECT * FROM alumnos;
"
