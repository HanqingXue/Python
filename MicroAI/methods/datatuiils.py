#coding = utf-8

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