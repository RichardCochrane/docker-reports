from flask import Flask

from app.db import setup_database


# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file
app.config.from_object('config')

setup_database()
