from flask import Flask, render_template


# showing taht we are creating a new web application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
