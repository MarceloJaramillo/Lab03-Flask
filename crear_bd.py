from db import get_connection

def crear_base_datos():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS administradores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            rol TEXT NOT NULL DEFAULT 'usuario'
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total = cursor.fetchone()[0]

    if total == 0:
        cursor.executemany("""
            INSERT INTO usuarios (nombre, email, rol)
            VALUES (?, ?, ?)
        """, [
            ("Juan Pérez", "juan.perez@gmail.com", "usuario"),
            ("María López", "maria.lopez@gmail.com", "admin"),
            ("Carlos Ramos", "carlos.ramos@gmail.com", "usuario")
        ])

    conexion.commit()
    cursor.close()
    conexion.close()

    print("Base de datos SQLite creada correctamente.")
    print("Archivo generado: lab03_flask.db")

if __name__ == "__main__":
    crear_base_datos()