
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def conectar_db():
    return mysql.connector.connect(
        host="mysql-devops",  # nombre del contenedor
        user="root",
        password="rootpass",
        database="devops_db"
    )

@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    conn = conectar_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM alumnos")
    alumnos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(alumnos)

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
    return jsonify({"mensaje": f"Alumno '{data['nombre']}' registrado correctamente", "id": id_nuevo}), 201

@app.route('/alumnos/<int:id>', methods=['PUT'])
def actualizar_alumno(id):
    data = request.json
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id,))
    alumno = cursor.fetchone()
    if not alumno:
        return jsonify({"error": "Alumno no encontrado"}), 404
    cursor.execute("UPDATE alumnos SET nombre = %s WHERE id = %s", (data['nombre'], id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": f"Alumno con id {id} actualizado correctamente"})

@app.route('/alumnos/<int:id>', methods=['DELETE'])
def eliminar_alumno(id):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alumnos WHERE id = %s", (id,))
    alumno = cursor.fetchone()
    if not alumno:
        return jsonify({"error": "Alumno no encontrado"}), 404
    cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"mensaje": f"Alumno con id {id} eliminado correctamente"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
