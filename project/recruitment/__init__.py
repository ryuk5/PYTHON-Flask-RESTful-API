from flask import Blueprint

blueprint = Blueprint(
    'recruitment_blueprint', # The name of my module
    __name__,
    url_prefix='/recruitment',
    template_folder='templates',
    static_folder='static'
)

from . import routes