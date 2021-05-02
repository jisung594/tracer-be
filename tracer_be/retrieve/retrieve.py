from flask import Blueprint, request, make_response
import requests
from config import Config

from flask_cors import CORS, cross_origin #--------------------

# Blueprint config
retrieve_bp = Blueprint(
    'retrieve_bp', __name__
)

api_key = Config.API_KEY

# CORS(retrieve_bp, resources={r"/*": {"origins": "http://localhost:3000"}},  supports_credentials=True) #-----------------------
# CORS(retrieve_bp) #------------------------


# STOCKS
@retrieve_bp.route('/stocks_us', methods=['GET'])
# @cross_origin(origins=['http://localhost:3000', 'https://tracerscfx.herokuapp.com'])
def list_stocks():
    # return requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=' + api_key).content

    # requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=' + api_key).content

    res = make_response(requests.get('https://finnhub.io/api/v1/stock/symbol?exchange=US&token=' + api_key).content)
    res.headers['Content-Type'] = 'application/json'
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Headers'] = '*'
    res.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    res.headers['Access-Control-Allow-Credentials'] = 'true'
    return res

# @retrieve_bp.after_request
# def after_request(response):
    # res.headers.add('Content-Type', 'application/json')
    # res.headers.add('Access-Control-Allow-Origin', '*')
    # res.headers.add('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    # res.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    # res.headers.add('Access-Control-Allow-Credentials', 'true')
#     return response




@retrieve_bp.route('/current_price', methods=['GET','POST'])
def get_price():
    if request.method == 'POST':
        req_obj = request.get_json()
        ticker = req_obj['symbol']

        return requests.get('https://finnhub.io/api/v1/quote?symbol=' + ticker + '&token=' + api_key).content

@retrieve_bp.route('/stock_info', methods=['GET','POST'])
def get_info():
    if request.method == 'POST':
        req_obj = request.get_json()
        ticker = req_obj['symbol']

        return requests.get('https://finnhub.io/api/v1/stock/profile2?symbol=' + ticker + '&token=' + api_key).content
# ------------------------------------------------------------------------------

# CRYPTO
@retrieve_bp.route('/crypto_exchanges', methods=['GET'])
def crypto_exchanges():
    return requests.get('https://finnhub.io/api/v1/crypto/exchange?token=' + api_key).content

@retrieve_bp.route('/cryptos_by_exchange', methods=['GET','POST'])
def list_crypto():
    # exchange = request.form['exchange']
    exchange = 'kraken' # *** placeholder ***
    return requests.get('https://finnhub.io/api/v1/crypto/symbol?exchange=' + exchange + '&token=' + api_key).content
# ------------------------------------------------------------------------------

# FOREX
@retrieve_bp.route('/fx_exchanges', methods=['GET'])
def fx_exchanges():
    return requests.get('https://finnhub.io/api/v1/forex/exchange?token=' + api_key).content

# @retrieve_bp.route('/fx_by_exchange', methods=['GET'])
# def list_fx():
