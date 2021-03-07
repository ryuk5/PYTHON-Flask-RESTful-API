from flask import Blueprint

blueprint = Blueprint(
    'lab_blueprint', # The name of my module
    __name__,
    url_prefix='/lab',
    template_folder='templates',
    static_folder='static'
)

from . import routes