import input

def process_input(puzzle_input):
	instructions = []
	dependents = []
	prerequisites = []
	firsts = []
	input_split = puzzle_input.split('\n')
	for i in input_split:
		prerequisite = i[i.find('Step') + 5]
		dependent = i[i.find('step', i.find('Step') + 5) + 5]
		if dependent in dependents:
			for r in instructions:
				if r[1] == dependent:
					r[0].append(prerequisite)
					break
		else:
			instructions.append([[prerequisite], dependent])
			dependents.append(dependent)
		if prerequisite not in prerequisites:
			prerequisites.append(prerequisite)
	for p in prerequisites:
		if p not in dependents:
			firsts.append(p)
	firsts.sort()
	return instructions, firsts, dependents


def process_steps(instructions, dependents, firsts):
	order = [firsts[0]]
	length = len(dependents) + len(firsts)
	while len(order) < length:
		available = []
		for f in firsts:
			if f not in order:
				available.append(f)
		for i in instructions:
			dependent_available = True
			for j in i[0]:
				if j not in order:
					dependent_available = False
					break
			if(dependent_available == True):
				if(i[1] in dependents and i[1] not in available): 
					available.append(i[1])
		available.sort()
	 	order.append(available[0])
	 	if(available[0] in dependents):
	 		dependents.remove(available[0])
	return ''.join(order)

instructions, firsts, dependents = process_input(input.puzzle_input)
order = process_steps(instructions, dependents, firsts)

print(order)