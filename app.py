import os
from flask import Flask
import config

app = Flask(__name__)
app.config.from_object('config.Config')

@app.route('/')
def hello_world():
    return os.environ.get('FLASK_ENV') or 'hello world'