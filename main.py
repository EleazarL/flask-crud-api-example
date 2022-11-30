from flask import Flask, json
import crud

app = Flask(__name__)

@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = crud.obtener_juegos()
    return str(datos)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
