from string import maketrans

puzzle = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "http://www.pythonchallenge.com/pc/def/map.html"

def decode(text):
	result = ""
	i = 0
	while i < len(text):
		if text[i].isalpha():
			coded_char = ord(text[i])
			if chr(coded_char+2).isalpha():
				result += chr(coded_char+2)
			else:
				result += chr(coded_char-24)
		else:
			result += text[i]
		i += 1
	return result

print decode(puzzle)
print decode(url)

# result says using string.maketrans() is recommmended, so that attempt is below. Achieves the result with much less code.

alpha = "abcdefghijklmnopqrstuvwxyz"
key = "cdefghijklmnopqrstuvwxyzab"

translation = maketrans(alpha, key)

print puzzle.translate(translation)