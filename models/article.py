import time
from sqlalchemy import Integer, UnicodeText
from sqlalchemy import Unicode, Column

from models.base_model import db, SQLMixin


class Article(SQLMixin, db.Model):
    views = Column(Integer, nullable=False, default=0)  # 访问量
    title = Column(Unicode(50), nullable=False)  # 文章标题
    content = Column(UnicodeText, nullable=False)  # 文章内容
    user_id = Column(Integer, nullable=False)  # 用户 id
    category_id = Column(Integer, nullable=False, default=0)  # 文章分类 id
