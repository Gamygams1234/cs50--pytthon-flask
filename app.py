from flask import Flask, render_template, request
import datetime


# showing taht we are creating a new web application
app = Flask(__name__)


@app.route("/")
def index():
    headline = "First Page"
    return render_template('index.html', headline=headline)


@app.route("/hello", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return "Please submit form instead"
    else:
        name = request.form.get("name")
        return render_template('hello.html', name=name)


@app.route("/names")
def names():
    names = ["John", "Jacob", "Reyes"]
    return render_template('names.html', names=names)


@app.route("/bye")
def bye():
    headline = "Bye everybody"
    return render_template('index.html', headline=headline)


@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template('newyear.html', new_year=new_year)
