from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required
#app.config["MYSQL_USER"] = "root"
#app.config["MYSQL_PASSWORD"] = "LtQm0b6CfxCZaGzx6aVd"
#app.config["MYSQL_DB"] = "railway"
#app.config["MYSQL_CURSORCLASS"] = "DictCursor"
#app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}

#mysql = MySQL(app)

@app.route("/")
def users():
   # cur = mysql.connection.cursor()
    #cur.execute("""SELECT * FROM login""")
    #rv = cur.fetchall()
    #return str(rv)
    return 'funciona'

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
