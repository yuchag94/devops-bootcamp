from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Función para conectar a la base de datos
def conectar_db():
    return mysql.connector.connect(
        host="mysql-devops",  # o tu host remoto si no es un contenedor
        user="root",
        password="rootpass",
        database="devops_db"
    )

# Ruta raíz para verificar que la API está viva
@app.route('/')
def home():
    return '¡API Flask funcionando correctamente en Render!'

# Ruta GET /alumnos para obtener todos los alumnos
@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    try:
        conn = conectar_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos")
        alumnos = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(alumnos)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

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

# Ejecutar en el puerto que Render espera
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
