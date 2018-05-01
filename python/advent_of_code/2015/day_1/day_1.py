import input

def traverse_building(floor, directions):
	i = 0
	entered_basement = False
	while i < len(directions):
		if directions[i] == '(':
			floor += 1
		elif directions[i] == ')':
			floor -= 1
		if entered_basement == False and floor < 0:
			print("First entered basement at position " + str(i+1))
			entered_basement = True
		i += 1
	return floor

print(traverse_building(0, input.puzzle_input))