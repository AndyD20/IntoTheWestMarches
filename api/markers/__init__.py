from flask import Blueprint

bp = Blueprint('markers', __name__)

from api.markers import markers