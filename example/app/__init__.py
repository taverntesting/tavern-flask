from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.get("/example")
    def get_example():
        return {}

    return app
