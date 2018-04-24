# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
from article_crawler import ArticleCrawler
import time

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

print('initializing bias analyzer')
start_time = time.time()
#analyzer = BiasAnalyzer()
analyzer = BiasAnalyzer(withSVM=False)
print('done')

################ WEB CONTENT ###################
urls = [
	'https://www.nytimes.com/2017/08/02/us/politics/trump-immigration.html',
	'']

crawler = ArticleCrawler()

for url in urls:
	paragraphs = crawler.url_content(url)
	# paragraphs = [['We should invest in healthcare and universal basic income.', 'Mehoy dude!']]

	# print(paragraphs)

	############## TESTING ARTICLE ANALYSIS ############
	# totalbias, total_dict = analyzer.get_article_bias(nyt_data)
	totalbias, total_dict = analyzer.get_article_bias(paragraphs)
	# print('done')
	print('analyzed in: ', str(time.time() - start_time))
	start_time = time.time()
	print('ANALYSIS RESULTS FOR ', url)
	print(totalbias)
	# print(total_dict)

