from flask import Flask, request, jsonify
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)

db_config = {
    'host': os.environ.get('MYSQL_HOST', 'db'),
    'user': os.environ.get('MYSQL_USER', 'root'),
    'password': os.environ.get('MYSQL_PASSWORD', 'rootpass'),
    'database': os.environ.get('MYSQL_DATABASE', 'devops_db')
}

@app.route('/alumnos', methods=['GET'])
def get_alumnos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, fecha_ingreso FROM alumnos")
    alumnos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([
        {"id": row[0], "nombre": row[1], "fecha_ingreso": str(row[2])}
        for row in alumnos
    ])

@app.route('/alumnos', methods=['POST'])
def create_alumno():
    data = request.get_json()
    nombre = data.get('nombre', 'Desconocido')
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO alumnos (nombre, fecha_ingreso) VALUES (%s, %s)",
        (nombre, datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": f"Alumno '{nombre}' registrado correctamente"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
