from flask import Blueprint, request
import requests
from config import Config

# Blueprint config
retrieve_bp = Blueprint(
    'retrieve_bp', __name__
)

@retrieve_bp.route('/stocks', methods=['GET'])
def list_stocks():
    api_key = Config.API_KEY
    return requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=' + api_key).content
