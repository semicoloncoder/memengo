from flask import Flask
import json, requests

app = Flask(__name__)

@app.route('/')
def indexPage():
    return 'Welcome to memengo app.'
