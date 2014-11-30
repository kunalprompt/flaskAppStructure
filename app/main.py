from flask import Flask, request, render_template, jsonify
from app import *
from views import *


if __name__=="__main__":
	app.run(debug=True)

