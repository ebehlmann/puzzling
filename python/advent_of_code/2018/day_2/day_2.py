import input

def parse_id(id):
	letters = {}
	i = 0
	while i < len(id):
		if id[i] in letters:
			letters[id[i]] += 1
		else:
			letters[id[i]] = 1
		i+=1
	return letters

def contains_set(parsed_id, size):
	for key in parsed_id:
		if parsed_id[key] == size:
			return True
	return False

def find_checksum(input, size_1, size_2):
	count_size_1 = 0
	count_size_2 = 0
	for i in input:
		parsed = parse_id(i)
		if contains_set(parsed, size_1):
			count_size_1 += 1
		if contains_set(parsed, size_2):
			count_size_2 += 1
	return count_size_1 * count_size_2

def one_different(id_1, id_2):
	differences = 0
	i = 0
	while i < len(id_1):
		if id_1[i] != id_2[i]:
			differences += 1
		if differences > 1:
			return False
		i += 1
	if differences == 1:
		return True
	return False

def find_one_different(input):
	i = 0
	while i < len(input) - 1:
		j = i + 1
		while j < len(input): 
			if one_different(input[i], input[j]) == True:
				return input[i], input[j]
			j += 1
		i += 1
	return ''

puzzle_input = input.puzzle_input.split('\n')

print('Checksum: ' + str(find_checksum(puzzle_input, 2, 3)))

print(find_one_different(puzzle_input))