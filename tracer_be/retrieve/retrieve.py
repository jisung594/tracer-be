from flask import Blueprint, request
import requests
from config import Config

# Blueprint config
retrieve_bp = Blueprint(
    'retrieve_bp', __name__
)


api_key = Config.API_KEY


# STOCKS
@retrieve_bp.route('/stocks_us', methods=['GET'])
def list_stocks():
    exchange= 'US' # *** placeholder ***
    return requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=' + exchange + '&token=' + api_key).content


# CRYPTO
@retrieve_bp.route('/crypto_exchanges', methods=['GET'])
def crypto_exchanges():
    return requests.get('https://finnhub.io/api/v1/crypto/exchange?token=' + api_key).content

@retrieve_bp.route('/cryptos_by_exchange', methods=['GET','POST'])
def list_crypto():
    # exchange = request.form['exchange']
    exchange = 'kraken' # *** placeholder ***
    return requests.get('https://finnhub.io/api/v1/crypto/symbol?exchange=' + exchange + '&token=' + api_key).content


# FOREX
@retrieve_bp.route('/fx_exchanges', methods=['GET'])
def fx_exchanges():
    return requests.get('https://finnhub.io/api/v1/forex/exchange?token=' + api_key).content

# @retrieve_bp.route('/fx_by_exchange', methods=['GET'])
# def list_fx():
