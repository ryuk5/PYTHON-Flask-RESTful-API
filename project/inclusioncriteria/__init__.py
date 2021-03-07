from flask import Blueprint

blueprint = Blueprint(
    'inclusioncriteria_blueprint', # The name of my module
    __name__,
    url_prefix='/inclusioncriteria',
    template_folder='templates',
    static_folder='static'
)

from . import routes