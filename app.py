from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from functools import wraps
from flask_cors import CORS
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
CORS(app)  # Permite que index.html (abierto directamente en el navegador) hable con este servidor


def conectar():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="security_toolkit"
    )

def login_requerido(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        if not session.get("admin"):
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorada

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    error = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        password = request.form.get("password")

        hash_password = generate_password_hash(password)

        conexion = conectar()
        cursor = conexion.cursor()

        try:
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, password_hash) VALUES (%s, %s, %s)",
                (nombre, correo, hash_password)
            )
            conexion.commit()
            cursor.close()
            conexion.close()
            return redirect(url_for("cuenta_login"))
        except mysql.connector.errors.IntegrityError:
            cursor.close()
            conexion.close()
            error = "Ese correo ya está registrado"

    return render_template("registro.html", error=error)


@app.route("/cuenta/login", methods=["GET", "POST"])
def cuenta_login():
    error = None
    if request.method == "POST":
        correo = request.form.get("correo")
        password = request.form.get("password")

        conexion = conectar()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()

        if usuario and check_password_hash(usuario["password_hash"], password):
            session["usuario_id"] = usuario["id"]
            session["usuario_nombre"] = usuario["nombre"]
            return redirect(url_for("inicio"))
        else:
            error = "Correo o contraseña incorrectos"

    return render_template("cuenta_login.html", error=error)


@app.route("/cuenta/logout")
def cuenta_logout():
    session.pop("usuario_id", None)
    session.pop("usuario_nombre", None)
    return redirect(url_for("inicio"))

@app.route("/admin")
@login_requerido
def admin():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reservas ORDER BY fecha_creacion DESC")
    reservas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("admin.html", reservas=reservas)

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        clave_ingresada = request.form.get("password")
        if clave_ingresada == os.getenv("ADMIN_PASSWORD"):
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            error = "Contraseña incorrecta"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))


@app.route("/reservar", methods=["POST"])
def reservar():
    if not session.get("usuario_id"):
        return jsonify({"error": "Debes iniciar sesión para reservar"}), 401

    datos = request.get_json()

    nombre = session.get("usuario_nombre")
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