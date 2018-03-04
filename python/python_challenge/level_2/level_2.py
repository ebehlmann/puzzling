import input
from collections import OrderedDict

def find_character_counts(text):
	characters = OrderedDict()
	i = 0
	while i < len(text):
		if text[i] not in characters:
			characters[text[i]] = 1
		else: 
			characters[text[i]] += 1
		i += 1
	return characters

def find_rare_characters(characters):
	result = []
	for key in characters:
		if characters[key] == 1:
			result.append(key)
	return result
 
characters = find_character_counts(input.text)

print find_rare_characters(characters)