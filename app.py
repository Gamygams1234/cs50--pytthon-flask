from flask import Flask, render_template
import datetime


# showing taht we are creating a new web application
app = Flask(__name__)


@app.route("/")
def index():
    headline = "Hello everybody"
    return render_template('index.html', headline=headline)


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"


@app.route("/bye")
def bye():
    headline = "Bye everybody"
    return render_template('index.html', headline=headline)


@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('newyear.html', new_year=new_year)
