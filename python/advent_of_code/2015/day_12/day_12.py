#this is incomplete

import json

def find_sum(mess_of_json):
	result = 0
	for i in mess_of_json:
		if type(i) == list:
			result += find_sum(i)
		elif type(i) == dict:
			result += find_sum(i)
		elif type(mess_of_json[i]) == int:
			result += mess_of_json[i]
	return result

#def find_sum_2(blob):


with open("input.json") as json_file:
    json_data = json.load(json_file)

    print(find_sum(json_data))