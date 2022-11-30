from flask import Flask, json
import controlador_juegos

app = Flask(__name__)

@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return str(datos)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
