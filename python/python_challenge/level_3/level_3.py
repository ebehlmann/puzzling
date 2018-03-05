import input

def isTargetText(some_text):
	uppers = some_text[1:4] + some_text[5:8]
	lowers = some_text[0] + some_text[4] + some_text[8]
	if uppers.isupper() == True and lowers.islower() == True:
		return True
	else:
		return False

def findInBlock(lots_of_text):
	i = 0
	results = ''
	while i < len(lots_of_text) - 8:
		segment = lots_of_text[i:i+9]
		if isTargetText(segment) == True:
			results += segment[4]
		i += 1
	return results

text = input.text.replace('\n', '')

print findInBlock(text)