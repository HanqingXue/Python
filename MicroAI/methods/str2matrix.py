#coding = utf-8

import numpy as np

def str2matrix(data, dim):
	data_list = data.split(',')
	data_num = [int(elm) for elm in data_list]
	row_num = len(data_num) / dim
	matrix =  np.array(data_num).reshape(row_num, dim)
	return matrix

def str2list(data):
	return str2matrix(data, 1)