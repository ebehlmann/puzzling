import input

def calculate_wrapping_paper(l, w, h):
	side_1 = l * w
	side_2 = w * h
	side_3 = l * h
	smallest = min(side_1, side_2, side_3)
	return 2*side_1 + 2*side_2 + 2*side_3 + smallest

def calculate_ribbon(l, w, h):
	dimensions = [l, w, h]
	dimensions.sort()
	wrap = dimensions[0]*2 + dimensions[1]*2
	cubic_feet = l * w * h
	return wrap + cubic_feet


def handle_packages(puzzle_input):
	wrapping_paper = 0
	ribbon = 0
	packages = puzzle_input.split('\n')
	for package in packages:
		dimensions = package.split('x')
		l = int(dimensions[0])
		w = int(dimensions[1])
		h = int(dimensions[2])
		wrapping_paper += calculate_wrapping_paper(l, w, h)
		ribbon += calculate_ribbon(l, w, h)
	return wrapping_paper, ribbon

paper, ribbon = handle_packages(input.puzzle_input)
print(str(paper) + ' square feet of paper')
print(str(ribbon) + ' feet of ribbon')
