#coding = utf-8

import tornado.web

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		algorithm = self.get_argument('algorithms')
		print algorithm
		self.render('result.html', algo = algorithm)