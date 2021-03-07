from flask import Blueprint

blueprint = Blueprint(
    'scheduledvisits_blueprint', # The name of my module
    __name__,
    url_prefix='/scheduledvisits',
    template_folder='templates',
    static_folder='static'
)

from . import routes