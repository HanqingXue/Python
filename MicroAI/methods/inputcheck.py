#coding = utf-8
'''
input : str  To check the datasets is valid.
return : bool 
'''
def is_vaild(input_value):
	input_to_list = input_value.split(',')
	input_to_set  = set(input_to_list)

	for item in input_to_set:
		if not item.isdigit():
			return False

	return True

def is_num_match(train_data):
	pass 



