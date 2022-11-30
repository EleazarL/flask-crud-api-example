from flask import Flask
from db import obtener_conexion

app = Flask(__name__)


@app.route("/")
def users():
    def obtener_juegos():
    conexion = obtener_conexion()
    datos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM login")
        datos = cursor.fetchall()
    conexion.close()
    return datos

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
