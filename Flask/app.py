from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/hello1")
def hello_world1():
    return "<h1>Hello, World!1</h1>"


@app.route("/hello2")
def hello_world2():
    return "<h1>Hello, World!2</h1>"


@app.route("/test_func")
def test():
    a = 5+6
    return "this is my first function in flask{}".format(a)


@app.route("/input_url")
def request_input():
    data = request.args.get('x')
    return "this is my input from url {}".format(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
