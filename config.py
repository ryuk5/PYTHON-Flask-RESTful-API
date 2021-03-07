# Here wew will create multiple mods that we are going to use for the application
from os import environ

# Here we will inherit from a base class
class Config(object):
    # Init SQLAlchemy config
    # Inside of this class we will init our SQLAlchemy db
    SQLALCHEMY_DATABASE_URI = environ.get( # We will try to grab an env variale
        'project_DATABASE_URL', # If this one failed we will use a sqlite database
        'sqlite:///database.sqlite3?check_same_thread=False' # Here I'm going to activate multi_threading
    )

    # Setting sqlalchemy track modifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Point this to my staging server
    DB_SERVER = '192.168.1.30'

class DebugConfig(Config):
    DEBUG = True
    SECRET_KEY = environ.get( # If our program fails to load the PROJECT_SECRET_KEY it loads the second value
        'PROJECT_SECRET_KEY', 'dont-rely-on-my-key'
    )

class ProductionConfig(Config):
    DEBUG = False
    DB_SERVER = '192.168.1.31' # This should points to our production server

    # Here we should force the user to provide a secret key
    SECRET_KEY = environ.get('PROJECT_SECRET_KEY')

    # In the production env we should have a vault where we are going to store 
    # the usernames, passwords, hashes...
    # !!! I will put my vault address
    VAULT_ADDRESS = environ.get('VAULT_ADDRESS')
    VAULT_TOKEN = environ.get('VAULT_TOKEN')

class TestingConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    SECRET_KEY = 'testkey'
    TESTING = True
    DATABASE_URI = 'sqlite:///:memory:' # We want to map our sqlite db to our memory


app_config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
    'Testing': TestingConfig
}