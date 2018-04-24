import json
from flask import Flask, Response, jsonify, request
from flask_cors import CORS
import urllib2
from modules.tf.bias_analyzer import BiasAnalyzer
from modules.article_crawler import ArticleCrawler

app = Flask(__name__)
CORS(app)

analyzer = BiasAnalyzer()

@app.route('/get_dict', methods=['GET'])
def get_bias_for_article():
    url = request.args['url']
    crawler = ArticleCrawler()
    paragraphs = crawler.url_content(url)
    print paragraphs
    totalbias, total_dict = analyzer.get_article_bias(paragraphs)
    return jsonify(dictionary=total_dict, total_bias=totalbias)