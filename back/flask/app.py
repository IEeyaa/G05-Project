from flask import Flask
import config
from exts import db
from flask_migrate import Migrate
from flask_cors import *
from blueprints import auth_bp, search_bp, result_bp

app = Flask(__name__)
app.config['DEBUG'] = True
# 绑定配置文件
app.config.from_object(config)
CORS(app, supports_credentials=True)
db.init_app(app)

migrate = Migrate(app, db)
app.register_blueprint(auth_bp)
app.register_blueprint(search_bp)
app.register_blueprint(result_bp)


@app.route('/')
def hello_world():  # put application's code here
    # engine = db.engine
    # conn = engine.connect()
    # result = conn.execute('select * from thesis')
    # print(result.fetchall())
    # conn.close()
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0")