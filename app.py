from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)  # Permite que index.html (abierto directamente en el navegador) hable con este servidor


def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="security_toolkit"
    )


@app.route("/reservar", methods=["POST"])
def reservar():
    datos = request.get_json()

    nombre = datos.get("nombre")
    servicio = datos.get("servicio")
    fecha = datos.get("fecha")
    hora = datos.get("hora")

    conexion = conectar()
    cursor = conexion.cursor()

    query = """
        INSERT INTO reservas (nombre, servicio, fecha, hora)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, servicio, fecha, hora))
    conexion.commit()

    cursor.close()
    conexion.close()

    return jsonify({"mensaje": "Reserva guardada correctamente"}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5000)