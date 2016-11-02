import numpy as np 
from  matplotlib import pyplot as plt 
from pyheatmap.heatmap import HeatMap

class drawHeatmap(object):
	"""docstring for drawHeatmap"""
	def __init__(self, dataname):
		super(drawHeatmap, self).__init__()
		self.dataname = dataname
		self.loaddata()
		
	def loaddata(self):
		self.data = np.loadtxt(self.dataname, delimiter=',')

	def draw(self):
		plt.pcolor(self.data)
		plt.show()
		pass

if __name__ == '__main__':
	heatmap = drawHeatmap('./data/Test1.csv')
	heatmap.draw()