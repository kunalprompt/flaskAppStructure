from flask import Flask
from app import *
from views import *
from models import *


if __name__=="__main__":
	app.run(debug=True)

