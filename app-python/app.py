from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Configura la conexión usando las variables de Railway
config = {
    'host': 'tramway.proxy.rlwy.net',
    'user': 'root',
    'password': 'yLaNXNWGkUGayEvHDtQEmdOjfvLcRqpL',
    'database': 'railway',
    'port': 59274
}

@app.route('/')
def home():
    return '¡API Flask funcionando correctamente en Render!'

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
