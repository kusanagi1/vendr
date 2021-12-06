import os

from flask import Flask


def create_app(test_config=None):
    # create an instance of Flask object
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="b2c0af7aca44fd2a02f8030d6bcd76db83675ab",
        DATABASE=os.path.join(app.instance_path, "blog.sqlite"),
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, Abiodun!"

    from . import db
    from . import auth
    from . import blog

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)

    return app
