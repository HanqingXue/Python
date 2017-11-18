#coding = utf-8

import tornado.web

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		algorithm = self.get_argument('algorithms')
		trainSample = self.get_argument('trainSample')
		trainLabel = self.get_argument('trainLabel')
		testSample = self.get_argument('testSample')

		if len(trainSample)  == 0 or  len(trainLabel) == 0 or len(testSample) == 0:
			self.render("error.html")
		else :
			self.render('result.html', algo = algorithm)