# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
from article_crawler import ArticleCrawler
import time
import cPickle

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

################ GET WEB CONTENT ###################
url = 'https://www.nytimes.com/2017/08/02/us/politics/trump-immigration.html'
# url = 'https://nypost.com/2018/04/21/democrats-are-getting-desperate-as-mueller-stalls/'
#url='http://www.foxnews.com/politics/2017/08/07/democrats-divided-over-whether-party-should-welcome-pro-life-candidates.html'
# url = 'http://www.breitbart.com/texas/2018/04/24/reports-caravan-migrants-waiting-cross-mexico-california-border/'
crawler = ArticleCrawler()


paragraphs = crawler.url_content(url)
# paragraphs = [['We should invest in healthcare and universal basic income.', 'Mehoy dude!']]

nyt_data = paragraphs
print(nyt_data)
#print(nyt_data)

############## INITIALIZING ANALYZER ###############
print('initializing bias analyzer')
start_time = time.time()
#analyzer = BiasAnalyzer()
analyzer = BiasAnalyzer(withSVM=False)
print('done')
print(str(time.time() - start_time))

start_time = time.time()

############## TESTING ARTICLE ANALYSIS ############
# totalbias, total_dict = analyzer.get_article_bias(nyt_data)
totalbias, total_dict = analyzer.get_article_bias(nyt_data)
print('done')
print(str(time.time() - start_time))
print('total bias index for the entire article')
print(totalbias)
print(total_dict)
