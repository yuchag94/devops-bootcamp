from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configura la conexión usando las variables de Railway
config = {
    'host': 'tramway.proxy.rlwy.net',
    'user': 'root',
    'password': 'yLaNXNWGkUGayEvHDtQEmdOjfvLcRqpL',
    'database': 'gestion_vehicular',
    'port': 59274
}

# HOME

@app.route('/')
def home():
    return '¡API Flask funcionando correctamente en Render!'

# VEHICULO

app.route('/vehiculo', methods=['POST'])
def agregar_vehiculo():
    data = request.json
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO vehiculo (tarjeta_propiedad, soat, poliza, revision, gps, clave_gps)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (data['tarjeta'], data['soat'], data['poliza'], data['revision'], data['gps'], data['clave_gps']))
    conexion.commit()
    return jsonify({"mensaje": "Vehículo agregado"}), 201

# PROPIETARIO

@app.route('/propietario', methods=['POST'])
def agregar_propietario():
    data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = """
            INSERT INTO propietario (cedula, rut, direccion, municipio, cuenta_bancaria, correo)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            data['cedula'],
            data['rut'],
            data['direccion'],
            data['municipio'],
            data['cuenta_bancaria'],
            data['correo']
        )
        cursor.execute(query, values)
        connection.commit()
        return jsonify({"mensaje": "Propietario agregado correctamente"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# CONDUCTOR 

@app.route('/conductor', methods=['POST'])
def agregar_conductor():
    data = request.json
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = """
            INSERT INTO conductor (cedula, direccion, municipio, licencia, correo, cuenta_bancaria, foto1, foto2)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['cedula'],
            data['direccion'],
            data['municipio'],
            data['licencia'],
            data['correo'],
            data['cuenta_bancaria'],
            data['foto1'],
            data['foto2']
        )
        cursor.execute(query, values)
        connection.commit()
        return jsonify({"mensaje": "Conductor agregado correctamente"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/alumnos')
def obtener_alumnos():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos")
        resultados = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(resultados)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)
