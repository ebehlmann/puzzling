import pickle
import urllib.request

file = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

unpickled = pickle.load(file)

for row in unpickled:
	row_text = ''
	for item in row:
		row_text += item[0] * item[1]
	print(row_text)