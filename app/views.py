from flask import Flask, request, render_template, jsonify
from app import *

@app.route('/', methods=['GET'])
def hello_world():
	return "Hello World!"