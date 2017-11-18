#coding = utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import json 
import tornado.web

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

			print train_matrix
			print test_matrix
			print train_label
			self.render('result.html', algo = algorithm)
		else:
			self.render("error.html")
			