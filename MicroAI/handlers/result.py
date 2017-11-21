#coding = utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import json

import tornado.web
import tornado.escape

from methods.datahelper import *
from methods.algohelper import *

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		algorithm = self.get_argument('algorithms')
		trainSample = self.get_argument('trainSample')

		result = json.loads(trainSample)
		
		train_data_status = is_vaild(result['trainData'])
		test_data_status = is_vaild(result['testData'])
		train_label_status = is_vaild(result['trainLabel'])

		if  train_data_status and test_data_status and train_label_status:
			train_data_list = result['trainData'].split(',')
			train_label_list = result['trainLabel'].split(',') 

			dim = len(train_data_list) / len(train_label_list) 
			train_matrix = str2matrix(result['trainData'], dim)
			test_matrix = str2matrix(result['testData'], dim)
			train_label = str2list(result['trainLabel'])
			
			series = format_test_series([list(item) for item in train_matrix], [item[0] for item in train_label])
			
			labels =  set([label[0] for label in train_label])
			legend = [ str(lbl) for lbl in list(labels)]

			algo = algohelper()
			#print algo.classify(algorithm, train_matrix, train_label, test_matrix)
			smpcnt = [train_matrix.shape[0], test_matrix.shape[0]]
			result = {
				'legend': legend,
				'time': 3,
				'recall': 90,
				'precision': 88,
				'fscore': 0.9,
				'smpcnt': smpcnt,
				'labelinfo': cnt_train_sample_size(train_label_list),
				'series': series
			}

			data = json.dumps(result)
			self.render('result.html', algo = algorithm, result = data)
		else:
			self.render("error.html")
			