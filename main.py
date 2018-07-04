#!usr/bin/env python3

import os, errno
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json(force=True)
    filename = data['source']

    if not filename:
        return "Invalid source", 400
    filename = os.path.join("dataset", filename + ".csv")

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    with open(filename, "a") as f:
        f.write(data['data'])

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=20000)

