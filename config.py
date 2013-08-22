from flask import Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)
