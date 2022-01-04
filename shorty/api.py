from flask import Blueprint, jsonify, request

from shorty.exception_handlers.shorty_exception_handler import ShortyExceptionHandler
from shorty.shorty_execution import ShortyExecution

api = Blueprint('api', __name__)


@api.route('/shortlinks', methods=['POST'])
def create_shortlink():
    data = request.get_json(force=True)
    short_link = ShortyExecution(data)
    provider_response = short_link.shorten_url()
    return jsonify(provider_response), 200


@api.errorhandler(ShortyExceptionHandler)
def error_handler(error):
    return jsonify(error.error_response()), error.status_code
