#coding = utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import json 
import tornado.web
from methods.inputcheck import is_vaild

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		algorithm = self.get_argument('algorithms')
		trainSample = self.get_argument('trainSample')

		result = json.loads(trainSample)
		train_data_status = is_vaild(result['trainData'])
		test_data_status = is_vaild(result['testData'])
		train_label_status = is_vaild(result['trainLabel'])

		if  train_data_status and test_data_status and train_label_status:
			self.render('result.html', algo = algorithm)
		else:
			self.render("error.html")
			