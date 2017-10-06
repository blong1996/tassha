from flask import Flask
from tassha_app.controllers import api_controllers as project_controllers

# Define app
app = Flask(__name__)

# Configurations
app.config.from_object('config')


# Register blueprints
def register_blueprints(app):
    app.register_bluprints(project_controllers)
