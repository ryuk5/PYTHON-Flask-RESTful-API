from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from os import environ
from pathlib import Path
from sys import exit

from config import app_config_dict
from project import create_app, db

get_config_mode = environ.get('PROJECT_CONFIG_MODE', 'Debug')

try:
    config_mode = app_config_dict[get_config_mode.capitalize()]
except KeyError:
    exit("Invalid Config Mode!")

app = create_app(Path.cwd(), config_mode)

db.init_app(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run() # If I want to run my migrations 
    # or
    # app.run()