import input

def process_sues(puzzle_input):
	sues = puzzle_input.split('\n')
	processed = {}
	for sue in sues:
		sue_data = {}
		split = sue.find(':')
		num = int(sue[4:split])
		info = sue[split+2:]
		info = info.split(', ')
		for item in info:
			item = item.split(': ')
			sue_data[item[0]] = int(item[1])
		processed[num] = sue_data
	return processed

def find_matching_sues(mfcsam_data, sues):
	for sue in sues:
		match = True
		for criterion in mfcsam_data:
			if criterion in sues[sue]:
				if mfcsam_data[criterion] != sues[sue][criterion]:
					match = False
					break
		if match == True:
			return sue
	return matches

def find_matching_sues_part_2(mfcsam_data, sues):
	for sue in sues:
		match = True
		for criterion in mfcsam_data:
			if criterion in sues[sue]:
				if criterion == 'cats' or criterion == 'trees':
					if sues[sue][criterion] <= mfcsam_data[criterion]:
						match = False
						break
				elif criterion == 'pomeranians' or criterion == 'goldfish':
					if sues[sue][criterion] >= mfcsam_data[criterion]:
						match = False
						break
				else:
					if mfcsam_data[criterion] != sues[sue][criterion]:
						match = False
						break
		if match == True:
			return sue
	return matches

sues = process_sues(input.puzzle_input)
mfcsam_data = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

print(find_matching_sues(mfcsam_data, sues))

print(find_matching_sues_part_2(mfcsam_data, sues))