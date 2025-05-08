from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Función para conectar a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="mysql-devops",  # nombre del contenedor o el host remoto
        user="root",
        password="rootpass",
        database="devops_db"
    )

# Ruta raíz para verificación
@app.route('/')
def home():
    return '¡API Flask funcionando correctamente en Render!'

# Obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    conn = conectar_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(alumnos)

# Agregar un nuevo alumno
@app.route('/alumnos', methods=['POST'])
def agregar_alumno():
    data = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alumnos (nombre) VALUES (%s)", (data['nombre'],))
    conn.commit()
    id_nuevo = cursor.lastrowid
    cursor.close()
    conn.close()
    return jsonify({"mensaje": "Alumno agregado", "id": id_nuevo})

# Ejecutar la app en el puerto 10000 (requerido por Render)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
