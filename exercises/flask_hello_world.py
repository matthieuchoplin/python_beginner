# ---- Flask Hello World ---- #
# import the Flask class from the flask package
import sqlite3
from flask import Flask, g
# create the application object
app = Flask(__name__)
# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/hello")
# define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"
@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"
# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return "Hello, {}".format(name), 200
    else :
        return "Not Found", 404

def connect_db():
    return sqlite3.connect("test_database.db")

@app.route('/persons')
def main():
    g.db = connect_db()
    cur = g.db.execute('select FirstName from People')
    persons = '\n'.join([p[0] for p in cur.fetchall()])
    g.db.close()
    return persons

# start the development server using the run() method
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)