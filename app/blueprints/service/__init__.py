from flask import Blueprint

service_bp = Blueprint('service', __name__, template_folder='service_templates')

from . import routes