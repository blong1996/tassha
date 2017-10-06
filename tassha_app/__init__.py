from flask import Flask
from tassha_app.controllers.api_controllers import tassha_api as tassha_api

# Define app
app = Flask(__name__)

# Configurations
app.config.from_object('config')


# Register blueprints
def register_blueprints(tassha_app):
    tassha_app.register_blueprint(tassha_api)


register_blueprints(app)
