from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("MYSQLHOST"),
    "user": os.getenv("MYSQLUSER"),
    "password": os.getenv("MYSQLPASSWORD"),
    "database": os.getenv("MYSQLDATABASE"),
    "port": int(os.getenv("MYSQLPORT"))
}

@app.route('/vehiculo', methods=['POST'])
def agregar_vehiculo():
    data = request.json
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO vehiculo (tarjeta_propiedad, soat, poliza, revision, gps, clave_gps)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data['tarjeta_propiedad'],
            data['soat'],
            data['poliza'],
            data['revision'],
            data['gps'],
            data['clave_gps']
        ))
        conn.commit()
        return jsonify({"mensaje": "Vehículo agregado"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/vehiculo', methods=['GET'])
def listar_vehiculos():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vehiculo")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
