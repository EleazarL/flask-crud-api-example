from db import obtener_conexion

def obtener_juegos():
    conexion = obtener_conexion()
    juegos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM login")
        juegos = cursor.fetchall()
    conexion.close()
    return juegos