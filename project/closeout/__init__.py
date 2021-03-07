from flask import Blueprint

blueprint = Blueprint(
    'closeout_blueprint', # The name of my module
    __name__,
    url_prefix='/closeout',
    template_folder='templates',
    static_folder='static'
)

from . import routes