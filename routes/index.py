from flask import Blueprint, render_template

main = Blueprint('index', __name__)


@main.route("/")
def index():
    message = "my first note"
    return render_template("index.html", message=message)
