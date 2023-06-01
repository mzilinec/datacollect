import os
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

datafile = "/var/www/html/conversation.txt"

@app.route('/capture/denisa', methods=['POST'])
def capture():
    dt = datetime.now().strftime("[%d.%m.%Y %H:%M:%S] ")
    
    data = request.get_json(force=True)
    if data["auth"] != "heslojekreslo":
        return 'Unauthorized', 401
    
    text = data["text"]
    text = text.replace("\n", " ")
    text = dt + text
    
    with open(datafile, "a") as fp:
        fp.write(text + "\n")
    return 'ok', 200

