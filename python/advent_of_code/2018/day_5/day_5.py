import input

def convert_to_asciis(input):
	asciis = []
	for c in input:
		asciis.append(ord(c))
	return asciis

def reduce_polymer(asciis):
	i = 0
	while i < len(asciis) - 1:
		if abs(asciis[i] - asciis[i+1]) == 32:
			del asciis[i:i+2]
			i = 0
		else:
			i += 1
	reduced = ''.join(map(chr, asciis))
	return reduced

def find_characters(input):
	lowered = input.lower()
	asciis = convert_to_asciis(lowered)
	characters = []
	for c in asciis:
		if c >= 97 and c <= 122 and c not in characters:
			characters.append(c)
	return characters

def remove_character(asciis, character):
	result = []
	for c in asciis:
		if c != character and c != character - 32:
			result.append(c)
	return result

def get_length_by_character(asciis, characters):
	lengths = {}
	for c in characters:
		asciis_temp = remove_character(asciis, c)
		reduced = reduce_polymer(asciis_temp)
		lengths[c] = len(reduced)
		print(chr(c), len(reduced))
	return lengths

def find_min(length_by_characters):
	min = float("inf")
	best = 0
	for i in length_by_characters:
		if length_by_characters[i] < min:
			best = i
			min = length_by_characters[i]
	return(chr(best), min)

puzzle_input = input.puzzle_input
#puzzle_input = 'dabAcCaCBAcCcaDA'
converted_input = convert_to_asciis(puzzle_input)
#print('Reduced polymer: ' + str(len(reduce_polymer(converted_input))))

characters = find_characters(puzzle_input)
length_by_characters = get_length_by_character(converted_input, characters)
character, min_length = find_min(length_by_characters)
print('Reduced polymer after ' + character + ' removal: ' + str(min_length))