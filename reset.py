from sqlalchemy import create_engine

from app import configured_app
from models.base_model import db
from models.article import Article


def reset_database():
    # 现在 mysql root 默认用 socket 来验证而不是密码
    uri = 'sqlite:///mydb.db'
    e = create_engine(uri, echo=True)

    # with e.connect() as c:
        # c.execute('DROP DATABASE IF EXISTS blog')
        # c.execute('CREATE DATABASE blog CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')
        # c.execute('USE blog')

    db.metadata.create_all(bind=e)


def generate_fake_date():
    with open('markdown_demo.md', encoding='utf8') as f:
        content = f.read()
    form1 = dict(
        title='Markdown Demo',
        content=content,
        user_id=0,
    )
    Article.new(form1)
    form2 = dict(
        title='第二篇文章',
        content='第二篇文章正文',
        user_id=0,
    )
    Article.new(form2)


if __name__ == '__main__':
    app = configured_app()
    with app.app_context():
        reset_database()
        generate_fake_date()
