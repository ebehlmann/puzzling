import pandas as pd
import input

def process_instruction(instruction):
	inst_split = instruction.split(' ')
	if inst_split[0] == 'toggle':
		direction = 'toggle'
		inst_split = inst_split[1:]
	else:
		direction = inst_split[1]
		inst_split = inst_split[2:]
	corner_1 = map(int, inst_split[0].split(','))
	corner_2 = map(int, inst_split[2].split(','))
	return direction, corner_1, corner_2

def toggle(grid, x, y):
	if(grid.iloc[x, y]) == 0:
		grid.iloc[x, y] = 1
	else:
		grid.iloc[x, y] = 0
	return grid

def follow_instruction(grid, instruction, corner_1, corner_2):
	i = corner_1[0]
	while i <= corner_2[0]:
		j = corner_1[1]
		while j <= corner_2[1]:
			if instruction == 'on':
				grid.iloc[i, j] = 1
			elif instruction == 'off':
				grid.iloc[i, j] = 0
			else:
				grid = toggle(grid, i, j)
			j += 1
		i += 1
	return grid

def follow_instruction_part_2(grid, instruction, corner_1, corner_2):
	i = corner_1[0]
	while i <= corner_2[0]:
		j = corner_1[1]
		while j <= corner_2[1]:
			if instruction == 'on':
				grid.iloc[i, j] += 1
			elif instruction == 'off':
				if grid.iloc[i, j] > 0:
					grid.iloc[i, j] -= 1
			else:
				grid.iloc[i, j] += 2
			j += 1
		i += 1
	return grid

instructions = input.puzzle_input.split('\n')

height = 1000
width = 1000
grid = pd.DataFrame(0, index=range(height), columns=range(width))

for instruction in instructions:
	direction, corner_1, corner_2 = process_instruction(instruction)
	print(corner_1)
	#grid = follow_instruction(grid, direction, corner_1, corner_2)
	grid = follow_instruction_part_2(grid, direction, corner_1, corner_2)

print(grid.sum().sum())