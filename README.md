# 📘 DevOps Bootcamp: Docker + MySQL

Este repositorio contiene una práctica completa de Docker Compose utilizando MySQL y un script Bash para interactuar con la base de datos. Aquí documentamos los comandos más importantes y aprendizajes clave.

---

## 🐳 Docker & Docker Compose

### 🚀 Comandos básicos

```bash
# Construir e iniciar contenedores en segundo plano
docker compose up -d

# Ver los contenedores activos
docker ps

# Detener todos los contenedores
docker compose down

# Ingresar al contenedor app en bash
docker exec -it script-logica bash

# Ingresar al contenedor MySQL
docker exec -it mysql-devops mysql -uroot -prootpass devops_db
```

### 🛠 Estructura de `docker-compose.yml`

```yaml
services:
  app:
    build: .
    container_name: script-logica
    depends_on:
      - db
    tty: true
    stdin_open: true

  db:
    image: mysql:8.0
    platform: linux/amd64
    container_name: mysql-devops
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: devops_db
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql

volumes:
  mysql-data:
```

---

## 🧪 SQL Básico

```sql
-- Crear tabla
CREATE TABLE alumnos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50),
  fecha_ingreso TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos
INSERT INTO alumnos (nombre) VALUES ('Julieta');

-- Consultar
SELECT * FROM alumnos;
```

### 🔧 Modificar tabla para activar AUTO\_INCREMENT si no se agregó al inicio

```sql
ALTER TABLE alumnos MODIFY id INT NOT NULL AUTO_INCREMENT;
```

---

## 📦 Respaldar y restaurar base de datos

### 📝 Crear respaldo

```bash
./respaldo.sh
```

Crea un archivo `.sql` dentro de la carpeta `respaldo/`.

### ♻ Restaurar respaldo

```bash
docker exec -i mysql-devops mysql -uroot -prootpass devops_db < respaldo/backup_archivo.sql
```

---

## 🧠 Notas importantes

* Usa `depends_on` para controlar el orden de arranque entre contenedores.
* `AUTO_INCREMENT` es obligatorio si quieres omitir la columna `id` al insertar.
* Puedes modificar el Dockerfile para instalar paquetes con `apt-get install`.
* Evita usar `ping` si no está instalado; puedes probar conectividad con comandos como `mysqladmin`.

---

## 📂 Estructura del proyecto

```
├── respaldo/                 # Carpeta de backups
├── Dockerfile                # Script para construir contenedor app
├── docker-compose.yml        # Orquestador de servicios
├── script-logica.sh          # Script bash para interactuar con MySQL
└── respaldo.sh               # Script bash para hacer backups
```

---

## ✅ Autor

Ejercicios realizados como parte del Bootcamp de DevOps 🚀

