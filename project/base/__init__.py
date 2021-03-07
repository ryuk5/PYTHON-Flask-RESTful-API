from flask import Blueprint

blueprint = Blueprint(
    'base_blueprint', # The name of my module
    __name__,
    url_prefix='/',
    template_folder='templates',
    static_folder='static'
)

from . import routes