from flask import Blueprint

blueprint = Blueprint(
    'radiology_blueprint', # The name of my module
    __name__,
    url_prefix='/radiology',
    template_folder='templates',
    static_folder='static'
)

from . import routes