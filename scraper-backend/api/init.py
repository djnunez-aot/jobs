from flask import Blueprint
from .routes import my_route_function

api_blueprint = Blueprint('api', __name__)
api_blueprint.route('/my_route', methods=['GET', 'POST'])(my_route_function)
