# 🚀 API CRUD con Python y Flask

> Un proyecto de ejemplo simple que demuestra cómo construir una API RESTful para operaciones CRUD (Crear, Leer, Actualizar, Borrar) utilizando el framework Flask.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## 📝 Descripción

Este repositorio contiene el código fuente de una API básica construida con Flask y conectada a una base de datos MySQL. Es una plantilla ideal para entender los fundamentos de la creación de endpoints, el manejo de peticiones HTTP y la interacción con una base de datos en un proyecto de Python.

## ✨ Características Principales

* **Crear:** Añadir nuevos registros a la base de datos.
* **Leer:** Obtener la lista completa de registros o un registro específico por su ID.
* **Actualizar:** Modificar la información de un registro existente.
* **Eliminar:** Borrar un registro de la base de datos.

## ⚙️ Instalación y Puesta en Marcha

Para ejecutar este proyecto en tu máquina local, sigue estos sencillos pasos:

```bash
# 1. Clona el repositorio
git clone [https://github.com/EleazarL/flask-crud-api-example.git](https://github.com/EleazarL/flask-crud-api-example.git)

# 2. Navega al directorio del proyecto
cd flask-crud-api-example

# 3. (Recomendado) Crea y activa un entorno virtual
# En Windows:
python -m venv venv
venv\Scripts\activate
# En macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# 4. Instala las dependencias del proyecto
pip install -r requirements.txt

# 5. Configura tu base de datos
# (Asegúrate de tener MySQL corriendo y crea una base de datos para el proyecto.
# Luego, actualiza los datos de conexión en el archivo db.py si es necesario).

# 6. Ejecuta la aplicación
python main.py
```

Una vez ejecutado, el servidor estará corriendo en `http://127.0.0.1:5000`.

## 📡 Uso de la API (Endpoints)

Puedes usar herramientas como Postman o `curl` para interactuar con los siguientes endpoints.

| Método HTTP | Endpoint           | Descripción                             |
| ----------- | ------------------ | --------------------------------------- |
| `GET`       | `/recursos`        | Obtiene una lista de todos los recursos. |
| `GET`       | `/recursos/<id>`   | Obtiene un recurso específico por su ID.  |
| `POST`      | `/recursos`        | Crea un nuevo recurso.                  |
| `PUT`       | `/recursos/<id>`   | Actualiza un recurso existente.         |
| `DELETE`    | `/recursos/<id>`   | Elimina un recurso por su ID.           |

**Nota:** Reemplaza `recursos` con el nombre real del recurso que manejas en tu API (ej: `/usuarios`, `/productos`, etc.).
