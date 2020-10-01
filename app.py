import os
from flask import Flask, jsonify
import config

app = Flask(__name__)
app.config.from_object('config.Config')

def health_check_ok():
    return 'Ok'

def health_check_boom():
	  raise SystemError # change to internal error

def leads():
	 return jsonify({'id': 1, 'status': 'accepted'})

# health API
app.add_url_rule('/health/ok', view_func=health_check_ok, methods=['GET'])
app.add_url_rule('/health/boom', view_func=health_check_boom, methods=['GET'])

# leads API
app.add_url_rule('/v1/leads', view_func=leads, methods=['GET'])
