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
	'https://www.buzzfeed.com/jenniferlutz/as-nationalists-win-so-do-the-separatists?utm_term=.vlG4JlNvl#.prOZknzln',
	'https://www.buzzfeed.com/mikhailkorostikov/the-honey-badger-doctrine?utm_term=.nxOro5ZQq#.ffQZlJQkD',
	'https://www.buzzfeed.com/zahrahirji/secret-science-epa-pruitt?utm_term=.er2pBM8nxE#.qg2D709Qmy',
	'https://patribotics.blog/2018/01/02/trump-russia-collusion-why-muellers-not-thinking-small/',
	'https://www.bustle.com/p/bernie-sanders-new-job-plan-wants-to-make-sure-every-american-who-wants-employment-is-hired-8877541',
	'http://www.palmerreport.com/analysis/hot-circle-garbage/9677/',
	'http://www.palmerreport.com/analysis/jr-michael-flynn-mike-pence/9654/',
	'https://www.huffingtonpost.com/entry/ronny-jackson-veterans-affairs-senate-hearing-delayed_us_5ade805ee4b0df502a4eb706',
	'http://occupydemocrats.com/2017/10/02/nra-sponsored-band-played-las-vegas-music-festival-right-shooting/',
	'http://bipartisanreport.com/2018/04/23/the-president-just-made-a-move-that-puts-america-in-global-danger-like-a-total-sucker/',
	'https://www.washingtonpost.com/blogs/erik-wemple/wp/2018/04/24/new-york-times-corrects-its-curious-example-of-a-far-right-conspiracy/?utm_term=.8c1a08dd498e']

crawler = ArticleCrawler()

url_to_vec = dict()

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
	url_to_vec[url] = totalbias
	print(totalbias)
	# print(total_dict)

print(url_to_vec)
