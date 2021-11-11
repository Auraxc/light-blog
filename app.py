from flask import Flask
from models.base_model import db
from routes.index import main as index_routes  # 这里我们从 routes 文件夹下的 index 引入 main, 并把它重命名为 index_routes，这样在注册的时候更直观

def configured_app():
    # 初始化 flask
    # 注册路由
    app = Flask(__name__)

    uri = 'mysql+pymysql://{}:{}@localhost/{}?charset=utf8mb4'.format(
        "root", "password", "db_name"
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 如果好奇 SQLAlchemy 具体执行了哪些语句，可以把 False 设为 True，就会在控制台输出具体语句了。
    db.init_app(app)
    register_routes(app)
    return app


def register_routes(app):
    # 注册路由
    app.register_blueprint(index_routes)


if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码，本地调试时设为 localhost 即可
    app = configured_app()

    config = dict(
        debug=True,
        host='localhost',
        port=3000,
        threaded=True,
    )
    app.run(**config)
