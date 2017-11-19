#coding = utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import json

import tornado.web
import tornado.escape

from methods.inputcheck import is_vaild
from methods.str2matrix import *

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		algorithm = self.get_argument('algorithms')
		trainSample = self.get_argument('trainSample')

		result = json.loads(trainSample)
		print result
		train_data_status = is_vaild(result['trainData'])
		test_data_status = is_vaild(result['testData'])
		train_label_status = is_vaild(result['trainLabel'])

		if  train_data_status and test_data_status and train_label_status:
			train_data_list = result['trainData'].split(',')
			train_label_list = result['trainLabel'].split(',') 

			dim = len(train_data_list) / len(train_label_list) 
			train_matrix = str2matrix(result['trainData'], dim)
			train_label = str2list(result['trainLabel'])
			test_matrix = str2matrix(result['testData'], dim)
		
			smpcnt = [train_matrix.shape[0], test_matrix.shape[0]]
			result = {
				'legend': ['1', '2'],
				'time': 3,
				'recall': 90,
				'precision': 88,
				'fscore': 0.9,
				'smpcnt': smpcnt
			}

			data = json.dumps(result)
			self.render('result.html', algo = algorithm, result = data)
		else:
			self.render("error.html")
			