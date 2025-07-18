from flask import Flask

app = Flask(__name__)

# Importing routes after initializing app
from app import routes
