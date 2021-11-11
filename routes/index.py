from flask import Blueprint, render_template

main = Blueprint('index', __name__)


@main.route("/")
def index():
    articles = [
        {"title": "文章1", "create_time": "2021-1-1", "preview": "正文开头嘟嘟嘟"},
        {"title": "文章2", "create_time": "2021-1-2", "preview": "正文开头嘟嘟嘟"}
    ]
    return render_template("index.html", articles=articles)
