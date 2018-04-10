import json
from flask import Flask, Response, jsonify, request
import urllib2
from modules.tf.bias_analyzer import BiasAnalyzer
from modules.article_crawler import ArticleCrawler


app = Flask(__name__)
crawler = ArticleCrawler()
analyzer = BiasAnalyzer()
# From the flask sqlalchemy configurations page on tracking modifications:
#   If set to True, Flask-SQLAlchemy will track modifications of objects and
#   emit signals. The default is None, which enables tracking but issues a
#   warning that it will be disabled by default in the future. This requires
#   extra memory and should be disabled if not needed.

@app.route('/urlf', methods=['GET'])
def get_bias_for_article():
    print request.args['url']
    print('here');
    return request.args['url']

@app.route('/content', methods=['POST'])
def hello():
    """
    Constructs a setting object from the POST request body and adds the new
    setting to the airdrop setting table. Then returns the set setting.

    Returns:
        flask.wrappers.Response: Response object containing a json
            representation of the current setting.
    """
    print('post')
