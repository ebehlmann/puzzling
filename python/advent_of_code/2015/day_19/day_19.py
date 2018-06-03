import input

def process_input(puzzle_input):
	replacements = {}
	data = puzzle_input.split('\n')
	for datum in data:
		datum = datum.split(' => ')
		if datum[0] not in replacements:
			replacements[datum[0]] = []
		replacements[datum[0]].append(datum[1])
	return replacements

def find_molecules(replacements, starting_molecule):
	molecules = []
	for r in replacements:
		i = 0
		while i < len(replacements[r]):
			new = replacements[r][i]
			starting_point = 0
			while True:
				to_replace = starting_molecule.find(r, starting_point)
				if to_replace == -1:
					break
				new_molecule = starting_molecule[:to_replace] + starting_molecule[to_replace:].replace(r, new, 1)
				if new_molecule not in molecules:
					molecules.append(new_molecule)
				starting_point = to_replace+1
			i+=1
	return molecules

replacements = process_input(input.puzzle_input)
molecules = find_molecules(replacements, input.molecule)
print(len(molecules))