import input

def follow_instruction(current_location, direction):
	if direction == '>':
		new_location = (current_location[0] + 1, current_location[1])
	elif direction == '<':
		new_location = (current_location[0] - 1, current_location[1])
	elif direction == '^':
		new_location = (current_location[0], current_location[1] + 1)
	else:
		new_location = (current_location[0], current_location[1] - 1)
	return new_location

def add_visit(visits, location):
	if location in visits:
		visits[location] += 1
	else:
		visits[location] = 1
	return visits

def track_visits(instructions):
	visits = {}
	current_location = (0, 0)
	visits[current_location] = 1
	for instruction in instructions:
		current_location = follow_instruction(current_location, instruction)
		visits = add_visit(visits, current_location)
	return visits

def track_visits_with_robo(instructions):
	visits = {}
	santa_location = (0, 0)
	robo_location = (0, 0)
	visits[(0, 0)] = 2
	i = 0
	while i < len(instructions):
		if i % 2 == 0:
			santa_location = follow_instruction(santa_location, instructions[i])
			visits = add_visit(visits, santa_location)
		else:
			robo_location = follow_instruction(robo_location, instructions[i])
			visits = add_visit(visits, robo_location)
		i += 1
	return visits


visits = track_visits(input.puzzle_input)
print(len(visits))

robo_visits = track_visits_with_robo(input.puzzle_input)
print(len(robo_visits))