import pymysql

def obtener_conexion():
    return pymysql.connect(host='containers-us-west-114.railway.app',
                                user='root',
                                password='LtQm0b6CfxCZaGzx6aVd',
                                db='railway')