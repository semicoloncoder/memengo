from flask import Flask
import json, requests

app = Flask(__name__)

@app.route('/')
def indexPage():
    return 'Welcome to memengo app.'

app.run(host = '0.0.0.0', port = 80)