from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash
from functools import wraps
from db import get_connection
import sqlite3

app = Flask(__name__)
app.secret_key = "clave_secreta_lab03_flask"


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "admin_id" not in session:
            flash("Debes iniciar sesión para acceder al sistema.", "warning")
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        password = request.form.get("password", "").strip()

        if not usuario or not password:
            flash("Debes ingresar usuario y contraseña.", "danger")
            return redirect(url_for("login"))

        conexion = get_connection()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM administradores WHERE usuario = ?",
            (usuario,)
        )
        admin = cursor.fetchone()

        cursor.close()
        conexion.close()

        if admin and check_password_hash(admin["password"], password):
            session["admin_id"] = admin["id"]
            session["admin_usuario"] = admin["usuario"]
            flash("Inicio de sesión exitoso.", "success")
            return redirect(url_for("dashboard"))

        flash("Usuario o contraseña incorrectos.", "danger")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) AS total FROM usuarios")
    total_usuarios = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM usuarios WHERE rol = 'admin'")
    total_admins = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM usuarios WHERE rol = 'usuario'")
    total_normales = cursor.fetchone()["total"]

    cursor.close()
    conexion.close()

    return render_template(
        "dashboard.html",
        total_usuarios=total_usuarios,
        total_admins=total_admins,
        total_normales=total_normales
    )


@app.route("/usuarios")
@login_required
def listar_usuarios():
    busqueda = request.args.get("buscar", "").strip()

    conexion = get_connection()
    cursor = conexion.cursor()

    if busqueda:
        cursor.execute(
            """
            SELECT * FROM usuarios
            WHERE nombre LIKE ? OR email LIKE ? OR rol LIKE ?
            ORDER BY id DESC
            """,
            (f"%{busqueda}%", f"%{busqueda}%", f"%{busqueda}%")
        )
    else:
        cursor.execute("SELECT * FROM usuarios ORDER BY id DESC")

    usuarios = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template("usuarios.html", usuarios=usuarios, busqueda=busqueda)


@app.route("/usuarios/crear", methods=["GET", "POST"])
@login_required
def crear_usuario():
    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        rol = request.form.get("rol", "").strip()

        if not nombre or not email or not rol:
            flash("Todos los campos son obligatorios.", "danger")
            return redirect(url_for("crear_usuario"))

        try:
            conexion = get_connection()
            cursor = conexion.cursor()

            cursor.execute(
                "INSERT INTO usuarios (nombre, email, rol) VALUES (?, ?, ?)",
                (nombre, email, rol)
            )
            conexion.commit()

            cursor.close()
            conexion.close()

            flash("Usuario creado correctamente.", "success")
            return redirect(url_for("listar_usuarios"))

        except sqlite3.IntegrityError:
            flash("El correo electrónico ya existe.", "danger")
            return redirect(url_for("crear_usuario"))

    return render_template("crear_usuario.html")


@app.route("/usuarios/editar/<int:id>", methods=["GET", "POST"])
@login_required
def editar_usuario(id):
    conexion = get_connection()
    cursor = conexion.cursor()

    if request.method == "POST":
        nombre = request.form.get("nombre", "").strip()
        email = request.form.get("email", "").strip()
        rol = request.form.get("rol", "").strip()

        if not nombre or not email or not rol:
            flash("Todos los campos son obligatorios.", "danger")
            return redirect(url_for("editar_usuario", id=id))

        try:
            cursor.execute(
                """
                UPDATE usuarios
                SET nombre = ?, email = ?, rol = ?
                WHERE id = ?
                """,
                (nombre, email, rol, id)
            )
            conexion.commit()

            flash("Usuario actualizado correctamente.", "success")
            return redirect(url_for("listar_usuarios"))

        except sqlite3.IntegrityError:
            flash("El correo electrónico ya existe.", "danger")
            return redirect(url_for("editar_usuario", id=id))

        finally:
            cursor.close()
            conexion.close()

    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
    usuario = cursor.fetchone()

    cursor.close()
    conexion.close()

    if not usuario:
        flash("Usuario no encontrado.", "danger")
        return redirect(url_for("listar_usuarios"))

    return render_template("editar_usuario.html", usuario=usuario)


@app.route("/usuarios/eliminar/<int:id>", methods=["POST"])
@login_required
def eliminar_usuario(id):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conexion.commit()

    cursor.close()
    conexion.close()

    flash("Usuario eliminado correctamente.", "success")
    return redirect(url_for("listar_usuarios"))


@app.route("/logout")
@login_required
def logout():
    session.clear()
    flash("Sesión cerrada correctamente.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    print("Iniciando aplicación Flask...")
    app.run(host="127.0.0.1", port=5000, debug=True)