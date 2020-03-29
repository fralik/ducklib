from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['POST', "GET"])
def is_license_valid():
    if request.method == "GET":
        return json.dumps({'success': False}), 200, {'ContentType':'application/json'}

    try:
        user = request.form["username"]
        pwd = request.form["password"]
        if (user == "user") and (pwd == "12345"):
            response = json.dumps({'success': True}), 200, {'ContentType':'application/json'}
        else:
            response = json.dumps({'success': False}), 200, {'ContentType':'application/json'}
    except KeyError:
            response = json.dumps({'success': False}), 200, {'ContentType':'application/json'}

    return response

