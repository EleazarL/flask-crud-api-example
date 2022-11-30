import pymysql

def obtener_conexion():
    return pymysql.connect(host='bbh4lfs9qgiqk5rmdcoq-mysql.services.clever-cloud.com',
                                user='u4paijab6cwvtlmp',
                                password='Ynmot5L3VsJsW3aJnHcL',
                                db='bbh4lfs9qgiqk5rmdcoq')