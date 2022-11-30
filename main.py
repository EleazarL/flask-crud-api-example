from flask import Flask
from bd import obtener_conexion

app = Flask(__name__)

def obtener_juegos():
    conexion = obtener_conexion()
    datos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM login")
        datos = cursor.fetchall()
    conexion.close()
    return datos

@app.route("/")
def users():
    return 'funciona'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
