from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_index():
    return "Hello World"


@app.route("/", methods=["POST"])
def post_index():
    d = request.json
    s = d['keyword']
    if s != None:
        return "Your keyword is {0}".format(s)
    else:
        return "I need your keyword"
