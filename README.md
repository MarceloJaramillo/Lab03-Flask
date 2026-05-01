# Lab03 Flask - Sistema de Login y CRUD de Usuarios

Este proyecto corresponde al Laboratorio 03 de Flask.  
La aplicación implementa un sistema web con autenticación de administrador y mantenimiento completo de usuarios mediante operaciones CRUD.

El sistema permite iniciar sesión, visualizar un panel administrativo y gestionar usuarios registrados en una base de datos local.

---

## Objetivo del proyecto

Desarrollar una aplicación web utilizando Flask que permita:

- Validar el ingreso de un administrador mediante usuario y contraseña.
- Mostrar un panel de administración luego del inicio de sesión.
- Registrar nuevos usuarios.
- Listar usuarios existentes.
- Editar la información de usuarios.
- Eliminar usuarios registrados.
- Utilizar una base de datos para almacenar la información.

---

## Funcionalidades principales

### 1. Login de administrador

La aplicación cuenta con una pantalla de inicio de sesión donde el administrador debe ingresar sus credenciales.

Credenciales de prueba:

```text
Usuario: admin
Contraseña: admin123
```

Si las credenciales son correctas, el sistema redirige al dashboard administrativo.  
Si son incorrectas, se muestra un mensaje de error.

---

### 2. Dashboard administrativo

Luego del login, el usuario accede a un panel principal donde puede visualizar:

- Total de usuarios registrados.
- Total de administradores.
- Total de usuarios normales.
- Accesos rápidos para gestionar usuarios.

---

### 3. Gestión de usuarios

La aplicación permite realizar las siguientes operaciones:

- Crear usuario.
- Listar usuarios.
- Buscar usuarios por nombre, correo o rol.
- Editar usuario.
- Eliminar usuario con confirmación.

Cada usuario tiene los siguientes campos:

| Campo | Descripción |
|---|---|
| ID | Identificador único |
| Nombre | Nombre completo del usuario |
| Email | Correo electrónico |
| Rol | Rol asignado: admin o usuario |

---

## Tecnologías utilizadas

- Python
- Flask
- SQLite
- HTML
- CSS
- Git
- GitHub

---

## Base de datos

El proyecto utiliza SQLite como base de datos local.

Debido a restricciones del equipo de trabajo no se utilizó una instalación local de MySQL. Sin embargo, se mantiene la misma lógica de base de datos, autenticación y CRUD.

Archivos relacionados con la base de datos:

| Archivo | Descripción |
|---|---|
| `crear_bd.py` | Script que crea la base de datos SQLite y las tablas necesarias |
| `crear_admin.py` | Script que crea o reinicia el usuario administrador |
| `database.sql` | Script SQL de referencia para la estructura de base de datos |
| `db.py` | Archivo de conexión a la base de datos |

El archivo `lab03_flask.db` se genera automáticamente al ejecutar:

```bash
python crear_bd.py
```

Por buenas prácticas, el archivo `.db` no se sube al repositorio porque puede recrearse con el script indicado.

---

## Estructura del proyecto

```text
Lab03-Flask/
│
├── app.py
├── db.py
├── crear_bd.py
├── crear_admin.py
├── database.sql
├── requirements.txt
├── README.md
├── .gitignore
│
├── static/
│   └── css/
│       └── styles.css
│
└── templates/
    ├── base.html
    ├── login.html
    ├── dashboard.html
    ├── usuarios.html
    ├── crear_usuario.html
    └── editar_usuario.html
```

---

## Descripción de archivos principales

### `app.py`

Archivo principal de la aplicación Flask.  
Contiene las rutas principales del sistema:

- `/` para login.
- `/dashboard` para el panel administrativo.
- `/usuarios` para listar usuarios.
- `/usuarios/crear` para crear usuarios.
- `/usuarios/editar/<id>` para editar usuarios.
- `/usuarios/eliminar/<id>` para eliminar usuarios.
- `/logout` para cerrar sesión.

---

### `db.py`

Contiene la función de conexión a la base de datos SQLite.

---

### `crear_bd.py`

Crea las tablas necesarias para el sistema:

- `administradores`
- `usuarios`

También inserta usuarios de prueba en la tabla `usuarios`.

---

### `crear_admin.py`

Crea el usuario administrador inicial para acceder al sistema.

Credenciales generadas:

```text
Usuario: admin
Contraseña: admin123
```

La contraseña se almacena de forma encriptada usando las funciones de seguridad de Werkzeug.

---

### `database.sql`

Archivo SQL de referencia que contiene la estructura equivalente de las tablas del sistema.

---

### `templates/`

Carpeta que contiene las vistas HTML utilizadas por Flask:

| Archivo | Descripción |
|---|---|
| `base.html` | Plantilla principal |
| `login.html` | Pantalla de inicio de sesión |
| `dashboard.html` | Panel administrativo |
| `usuarios.html` | Listado y búsqueda de usuarios |
| `crear_usuario.html` | Formulario para crear usuarios |
| `editar_usuario.html` | Formulario para editar usuarios |

---

### `static/css/styles.css`

Archivo CSS principal del proyecto.  
Contiene el diseño visual de la aplicación, incluyendo:

- Login.
- Dashboard.
- Tarjetas de resumen.
- Tabla de usuarios.
- Formularios.
- Botones.
- Mensajes de alerta.

---

## Requisitos previos

Antes de ejecutar el proyecto se necesita tener instalado:

- Python 3
- Git
- Visual Studio Code o cualquier editor de código

Para verificar si Python está instalado, ejecutar:

```bash
python --version
```

o:

```bash
py --version
```

---

## Instalación del proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/MarceloJaramillo/Lab03-Flask.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd Lab03-Flask
```

### 3. Crear entorno virtual

```bash
py -m venv venv
```

### 4. Activar entorno virtual en Windows

```bash
.\venv\Scripts\Activate.ps1
```

Si se utiliza Git Bash, se puede activar con:

```bash
source venv/Scripts/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configuración de la base de datos

### 1. Crear la base de datos

Ejecutar:

```bash
python crear_bd.py
```

Este comando genera el archivo:

```text
lab03_flask.db
```

y crea las tablas necesarias.

### 2. Crear usuario administrador

Ejecutar:

```bash
python crear_admin.py
```

Este comando crea el usuario administrador para iniciar sesión.

---

## Ejecución de la aplicación

Para iniciar la aplicación, ejecutar:

```bash
python -m flask --app app run --debug
```

También se puede ejecutar con:

```bash
python app.py
```

Luego abrir el navegador e ingresar a:

```text
http://127.0.0.1:5000
```

---

## Credenciales de acceso

```text
Usuario: admin
Contraseña: admin123
```

---

## Uso de la aplicación

### Login

1. Ingresar a `http://127.0.0.1:5000`.
2. Escribir usuario y contraseña.
3. Presionar el botón ingresar.

### Dashboard

Después del login, se muestra el panel administrativo con indicadores de usuarios.

### Gestión de usuarios

Desde el botón “Gestionar usuarios” se puede:

- Visualizar usuarios registrados.
- Buscar usuarios.
- Crear un nuevo usuario.
- Editar un usuario existente.
- Eliminar un usuario.

---

## Flujo general del sistema

```text
Usuario ingresa al login
        ↓
Flask recibe usuario y contraseña
        ↓
Se consulta la tabla administradores
        ↓
Si las credenciales son correctas, se inicia sesión
        ↓
Se muestra el dashboard
        ↓
El administrador gestiona usuarios mediante CRUD
```

---

## Rutas principales

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET / POST | Login del administrador |
| `/dashboard` | GET | Panel principal |
| `/usuarios` | GET | Listado y búsqueda de usuarios |
| `/usuarios/crear` | GET / POST | Crear usuario |
| `/usuarios/editar/<id>` | GET / POST | Editar usuario |
| `/usuarios/eliminar/<id>` | POST | Eliminar usuario |
| `/logout` | GET | Cerrar sesión |

---

## Seguridad básica implementada

El proyecto incluye:

- Contraseña de administrador encriptada.
- Validación de sesión.
- Protección de rutas mediante decorador `login_required`.
- Validación de campos obligatorios.
- Confirmación antes de eliminar usuarios.
- Control de correos duplicados.

---

## Archivos ignorados por Git

El archivo `.gitignore` evita subir archivos innecesarios como:

```text
venv/
__pycache__/
*.pyc
.env
instance/
*.db
```

Esto permite que el repositorio tenga solo el código fuente y archivos necesarios para ejecutar el proyecto.

---

## Video demostrativo

El video de demostración debe mostrar:

1. Inicio de la aplicación.
2. Login con credenciales incorrectas.
3. Login con credenciales correctas.
4. Visualización del dashboard.
5. Listado de usuarios.
6. Creación de usuario.
7. Edición de usuario.
8. Eliminación de usuario.
9. Cierre de sesión.

---

## Autor

Desarrollado por:

```text
Marcelo Jaramillo
```

---

## Repositorio

```text
https://github.com/MarceloJaramillo/Lab03-Flask
```
