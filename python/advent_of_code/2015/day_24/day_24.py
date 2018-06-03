import input

def process_input(puzzle_input):
	split = puzzle_input.split('\n')
	gifts = []
	for i in split:
		gifts.append(int(i))
	return gifts

def get_per_side_weight(gifts, sides):
	weight = sum(gifts)
	return weight/sides

gifts = process_input(input.puzzle_input)
print(get_per_side_weight(gifts, 3))