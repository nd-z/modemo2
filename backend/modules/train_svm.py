# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
from article_crawler import ArticleCrawler
import time
import cPickle

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

############## INITIALIZING ANALYZER ###############
print('initializing bias analyzer')
start_time = time.time()
#analyzer = BiasAnalyzer()
analyzer = BiasAnalyzer(withSVM=True)
print('done')
print(str(time.time() - start_time))

start_time = time.time()

analyzer.train_SVM()
print('done training')
print(str(time.time() - start_time))
