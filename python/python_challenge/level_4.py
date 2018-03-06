import urllib.request
import urllib.parse

""" input info:
http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
and the next nothing is 44827
"""

base = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

def make_url(base, params, values):
	data = {}
	for param, value in zip(params, values):
		data[param] = value
	url_data = urllib.parse.urlencode(data)
	return base + "?" + url_data

def get_value(text):
	start = text.find("the next nothing is")
	value = ''
	for c in text[start:]:
		if c.isdigit() == True:
			value += c
	return value

i = 0
nothing = 12345

while i < 400:
	url = make_url(base, ["nothing"], [nothing])
	response = urllib.request.urlopen(url)
	text = response.read().decode("utf-8")

	if "Divide by two and keep going" in text:
		nothing = str(int(nothing) / 2)
	else:
		nothing = get_value(text)

	if len(nothing) == 0:
		print(text)
		break

	i += 1
	