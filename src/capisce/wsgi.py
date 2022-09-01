#!/usr/bin/env python3
# -*- encoding:utf-8 -*-

import webbrowser

from flask import (Flask, Response, render_template, request,
                   send_from_directory)
from flask_cors import CORS
from ratelimit import limits, sleep_and_retry

from capisce.req import Req

app = Flask(__name__)
app.req = Req()
CORS(app)

_CALLS = 100
_PERIOD = 60

webbrowser.open('http://127.0.0.1:5000', new=2)


@app.route("/")
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def index():
    return render_template("index.html")


@app.route("/get", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def get():
    if ('endpoint' and 'headers') not in request.json.keys():
        return Response(status=400)

    response = app.req.get(request.json['endpoint'], request.json['headers'])
    return response


@app.route("/head", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def head():
    if ('endpoint' and 'headers') not in request.json.keys():
        return Response(status=400)

    response = app.req.head(request.json['endpoint'], request.json['headers'])
    return response


@app.route("/post", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def post():
    if ('endpoint' and 'headers' and 'body') not in request.json.keys():
        return Response(status=400)

    response = app.req.post(
        request.json['endpoint'], request.json['headers'], request.json['body'])
    return response


@app.route("/put", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def put():
    if ('endpoint' and 'headers' and 'body') not in request.json.keys():
        return Response(status=400)

    response = app.req.put(
        request.json['endpoint'], request.json['headers'], request.json['body'])
    return response


@app.route("/delete", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def delete():
    if ('endpoint' and 'headers' and 'body') not in request.json.keys():
        return Response(status=400)

    response = app.req.delete(
        request.json['endpoint'], request.json['headers'], request.json['body'])
    return response


@app.route("/options", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def options():
    if ('endpoint' and 'headers') not in request.json.keys():
        return Response(status=400)

    response = app.req.options(
        request.json['endpoint'], request.json['headers'])
    return response


@app.route("/patch", methods=['POST'])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def patch():
    if ('endpoint' and 'headers' and 'body') not in request.json.keys():
        return Response(status=400)

    response = app.req.options(
        request.json['endpoint'], request.json['headers'], request.json['body'])
    return response

# Assets


@app.route("/assets/<path:path>", methods=["GET"])
@sleep_and_retry
@limits(calls=_CALLS, period=_PERIOD)
def serve_static_files(path):
    return send_from_directory('templates/assets', path)


def main():
    app.run(host='127.0.0.1', port='5000')


if __name__ == "__main__":
    main()
