from flask import Blueprint
from .routes import scrape

api_blueprint = Blueprint('api', __name__)
api_blueprint.route('/scrape', methods=['POST'])(scrape)
