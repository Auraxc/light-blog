from flask import Blueprint, render_template

from models.article import Article

main = Blueprint('article', __name__)


@main.route("/<article_id>")
def index(article_id):
    print("article id", article_id)
    article = Article.one(id=article_id)
    return render_template("article.html", article=article)
