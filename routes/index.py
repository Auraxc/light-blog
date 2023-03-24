from flask import Blueprint, render_template

from models.article import Article

main = Blueprint('index', __name__)


@main.route("/")
def index():
    articles = Article.all()
    return render_template("index.html", articles=articles)


@main.route("/about_me")
def about_me():
    return "code forever"
