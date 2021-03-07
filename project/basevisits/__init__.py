from flask import Blueprint

blueprint = Blueprint(
    'basevisits_blueprint', # The name of my module
    __name__,
    url_prefix='/basevisits',
    template_folder='templates',
    static_folder='static'
)

from . import routes