import json
from flask import Flask, Response, jsonify, request
import urllib2
from modules.tf.bias_analyzer import BiasAnalyzer
from modules.article_crawler import ArticleCrawler


app = Flask(__name__)
crawler = ArticleCrawler()
analyzer = BiasAnalyzer()

@app.route('/get_dict', methods=['GET'])
def get_bias_for_article():
    url = request.args['url']
    paragraphs = crawler.url_content(url)
    nyt_data = paragraphs
    totalbias, total_dict = analyzer.get_article_bias(nyt_data)
    return jsonify(dictionary=total_dict, total_bias=totalbias)