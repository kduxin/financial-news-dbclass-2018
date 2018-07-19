# -*- coding:utf-8 -*-

from flask import Flask
from flask import request
import json
import services
app = Flask(__name__)

svs = services.service()

@app.route("/")
def hello():
    return "杜鑫大帅逼!"

@app.route('/api/hotwords', methods = ['GET'])
def get_hotwords():
    days = request.args.get('days', type = int)
    ### TODO
    return '你申请了%d天的热词数据.'%days

@app.route('/api/word_temperature', methods = ['GET'])
def get_word_temperature():
    days = request.args.get('days', type = int)
    word = request.args.get('word', type = str)
    ### TODO
    return '你申请了%d天内%s这个词的热度数据.'%(days, word)

@app.route('/api/stock_index', methods = ['GET'])
def get_stock_index():
    ### TODO
    return '你申请了股指数据.'

@app.route('/api/newest_article', methods = ['GET'])
def get_newest_article():
    return svs.get_newest_article()

@app.route('/api/recent_hotwords', methods = ['GET'])
def get_recent_hotwords():
    articles = svs.get_recent_articles()
    articles_inone = '.'.join(list(map(lambda x:x[2], articles)))
    hotwords = svs.get_keywords(articles_inone)
    return json.dumps(hotwords)

if __name__ == "__main__":
    app.run(port = 5000)