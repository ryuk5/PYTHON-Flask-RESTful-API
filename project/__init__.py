# In this file where we are going to register our blueprints recursively !!!
from flask import Flask, blueprints
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from hvac import Client as VaultClient
from flask_marshmallow import Marshmallow

db = SQLAlchemy(session_options={"expire_on_commit": False})

# Initialize our marshmallow
ma = Marshmallow()

# enregistrement btari9a récursive
def register_blueprints(app): 
    # Here we put the names of our folders
    blueprints = (
        'base',
        'admin',
        'followupvisits',
        'inclusioncriteria',
        'lab',
        'radiology',
        'recruitment',
        'scheduledvisits',
        'users',
        'basevisits',
        'closeout'
    )

    for blueprint in blueprints:
        # I want to import my modules recursively
        module = import_module(f'project.{blueprint}')

        # Registering the blueprint
        app.register_blueprint(module.blueprint)

        # print(f'===> blueprint for {blueprint} registered')

def create_vault_client(app):
    return VaultClient(
        url=app.config('VAULT_ADDRESS'),
        token=app.config('VAULT_TOKEN')
    )


#------------------------------------------------------------------------------------
# Import our schemas
from . users.models import User as user_model
from . users.fakedata import fake_data
# Here we will configure our database
def configure_database(app):
    # Here we will create our database
    @app.before_first_request
    def create_default():
        # When some one sends the first request I wanna create the Database
        db.create_all()
        # The user table will be created when the first request is sent to the server
        user_model.metadata.create_all(bind=db.engine)
        # Create fake data on the first request coming to the server
        # fake_data(100) # We just created 100 fake record

#------------------------------------------------------------------------------------

# I need to create my application
def create_app(path, config):
    # We need to start by creating a config file first
    app = Flask(__name__, static_folder='base/static') # I set this if I'm going to render templates
    app.config.from_object(config)

    # When we are creating our app we will grab our config object
    app.production = not app.config['DEBUG'] # In production we don't debug

    app.path = path

    # Registering our blueprints
    register_blueprints(app)

    # Configure our DB
    configure_database(app)

    # We will check if we are in production
    if app.production:
        # We will try to read our details from the client (houni no9sod fél env variables)
        app.vault_client = create_vault_client(app)

    return app
