from flask import Blueprint, render_template

from models.article import Article

main = Blueprint('index', __name__)


@main.route("/")
def index():
    articles = Article.all()
    return render_template("index.html", articles=articles)
