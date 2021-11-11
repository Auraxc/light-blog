import time
from sqlalchemy import Integer, UnicodeText
from sqlalchemy import Unicode, Column

from models.base_model import db, SQLMixin


class Article(SQLMixin, db.Model):
    views = Column(Integer, nullable=False, default=0)
    title = Column(Unicode(50), nullable=False)
    content = Column(UnicodeText, nullable=False)
    user_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
