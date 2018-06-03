import input

def process_input(puzzle_input):
	split = puzzle_input.split('\n')
	instructions = []
	for i in split:
		i = i.split(' ')
		if i[0] == 'jio' or i[0] == 'jie':
			i[1] = i[1][0:1]
			if i[2][0] == '+':
				i[2] = int(i[2][1:])
			else:
				i[2] = int(i[2][1:]) * -1
		elif i[0] == 'jmp':
			if i[1][0] == '+':
				i[1] = int(i[1][1:])
			else:
				i[1] = int(i[1][1:]) * -1
		instructions.append(i)
	return instructions

def run_instructions(instructions, a, b):
	i = 0
	iterations = 0 
	while i >= 0 and i < len(instructions):
		if instructions[i][0] == 'hlf':
			if instructions[i][1] == 'a':
				a = a/2
			else:
				b = b/2
			i += 1
		elif instructions[i][0] == 'tpl':
			if instructions[i][1] == 'a':
				a = a * 3
			else: 
				b = b * 3
			i += 1
		elif instructions[i][0] == 'inc':
			if instructions[i][1] == 'a':
				a += 1
			else:
				b += 1
			i += 1
		elif instructions[i][0] == 'jmp':
			i += instructions[i][1]
		elif instructions[i][0] == 'jie':
			if instructions[i][1] == 'a':
				if a % 2 == 0:
					i += instructions[i][2]
				else: 
					i += 1
			else:
				if b % 2 == 0:
					i += instructions[i][2]
				else:
					i += 1
		else: 
			if instructions[i][1] == 'a':
				if a == 1:
					i += instructions[i][2]
				else: 
					i += 1
			else:
				if b == 1:
					i += instructions[i][2]
				else:
					i += 1
	return a, b

instructions = process_input(input.puzzle_input)
print(run_instructions(instructions, 0, 0))
print(run_instructions(instructions, 1, 0))