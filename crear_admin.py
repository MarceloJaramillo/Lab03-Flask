from werkzeug.security import generate_password_hash
from db import get_connection

def crear_admin():
    usuario = "admin"
    password = "admin123"
    password_hash = generate_password_hash(password)

    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS administradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("DELETE FROM administradores WHERE usuario = ?", (usuario,))

    cursor.execute(
        "INSERT INTO administradores (usuario, password) VALUES (?, ?)",
        (usuario, password_hash)
    )

    conexion.commit()
    cursor.close()
    conexion.close()

    print("Administrador reseteado correctamente.")
    print("Usuario: admin")
    print("Contraseña: admin123")

if __name__ == "__main__":
    crear_admin()