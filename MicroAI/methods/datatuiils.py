#coding = utf-8
'''
lbllist: the list object of lalbel trian labels
'''
def cnt_train_sample_size(lbl_list):
	lbl_set = set(lbl_list)
	lbl_cnt = []
	
	for lbl in lbl_set:
		lbl_num = lbl_list.count(lbl)
		lbl_cnt.append({
			'value' : lbl_num,
			'name'  : lbl
			})

	piedata = {
		"legend": list(lbl_set),
		"data": lbl_cnt
	}
	return piedata

'''
data : test data
lbls : predicted labels 
'''
def format_test_series(data, lbls):
	cls_result = {}
	for point, lbl in zip(data, lbls):
		if lbl not in cls_result.keys():
			cls_result[lbl] = []
			cls_result[lbl].append(point)
		else:
			cls_result[lbl].append(point)

 	series = []
 	
 	for name in cls_result.keys():
 		series.append({
 			'name' : name,
 			'data' : cls_result[name],
 			'type' : 'scatter'
 			})
	
	return series