#coding = utf-8
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import json 
import tornado.web

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		algorithm = self.get_argument('algorithms')
		trainSample = self.get_argument('trainSample')

		result = json.loads(trainSample)
		print result

		if len(trainSample)  == 0:
			self.render("error.html")
		else :
			self.render('result.html', algo = algorithm)