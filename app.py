from flask import Flask


# showing taht we are creating a new web application
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"
