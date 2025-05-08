from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración de conexión a MySQL
db_config = {
    'host': 'localhost',           # Cambia si tu base de datos está en otro servidor
    'user': 'tu_usuario',
    'password': 'tu_contraseña',
    'database': 'nombre_base_datos'
}

@app.route('/')
def inicio():
    return '¡API Flask funcionando correctamente en Render!'

@app.route('/alumnos', methods=['GET'])
def obtener_alumnos():
    try:
        conexion = mysql.connector.connect(**db_config)
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM alumnos")
        resultados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify(resultados)
    except mysql.connector.Error as error:
        return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
