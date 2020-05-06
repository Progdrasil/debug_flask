from flask import Flask

__version__ = "0.1.0"
app = Flask(__name__)


@app.route("/")
def hello_debug():
    return {"Hello": "Debug"}


@app.route("/test-reload")
def reload():
    return {"reloading": "should not work"}


@app.route("test")
def test():
    return "test"
