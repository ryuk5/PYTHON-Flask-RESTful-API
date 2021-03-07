from flask import Blueprint

blueprint = Blueprint(
    'admin_blueprint', # The name of my module
    __name__,
    url_prefix='/admin',
    template_folder='templates',
    static_folder='static'
)

from . import routes