from flask import Blueprint

blueprint = Blueprint(
    'followupvisits_blueprint', # The name of my module
    __name__,
    url_prefix='/followupvisits',
    template_folder='templates',
    static_folder='static'
)

from . import routes