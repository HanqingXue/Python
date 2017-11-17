#coding = utf-8

import tornado.web

class ResultHandler(tornado.web.RequestHandler):
	def post(self):
		self.render('index.html')