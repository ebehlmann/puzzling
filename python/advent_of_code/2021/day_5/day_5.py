import numpy as np
import csv


class Line():
	def __init__(self, start, end):
		self.x_start = int(start.split(',')[0])
		self.y_start = int(start.split(',')[1])
		self.x_end = int(end.split(',')[0])
		self.y_end = int(end.split(',')[1])
		self.max = max(self.x_start, self.x_end, self.y_start, self.y_end)

	def is_vertical(self):
		return self.x_start == self.x_end

	def is_horizontal(self):
		return self.y_start == self.y_end

	def is_diagonal(self):
		return abs(self.x_end - self.x_start) == abs(self.y_end - self.y_start)

	def apply_to_grid_horizontal(self, grid):
		x = min(self.x_start, self.x_end)
		while x <= max(self.x_start, self.x_end):
			grid[self.y_start, x] = grid[self.y_start, x] + 1
			x += 1
		return grid

	def apply_to_grid_vertical(self, grid): 
		y = min(self.y_start, self.y_end)
		while y <= max(self.y_start, self.y_end):
			grid[y, self.x_start] = grid[y, self.x_start] + 1
			y += 1
		return grid

	def apply_to_grid_diagonal(self, grid):
		if self.x_start < self.x_end:
			x = self.x_start
			max_x = self.x_end
			y = self.y_start
			y_at_end = self.y_end
		else:
			x = self.x_end
			max_x = self.x_start
			y = self.y_end
			y_at_end = self.y_start
		if y < y_at_end:
			y_direction = 'up'
		else:
			y_direction = 'down'
		while x <= max_x:
			grid[y, x] = grid[y, x] + 1
			x += 1
			if y_direction == 'up':
				y += 1
			else:
				y -= 1
		return grid

	def apply_to_grid(self, grid, include_diagonals=True):
		if self.is_vertical():
			grid = self.apply_to_grid_vertical(grid)
		elif self.is_horizontal():
			grid = self.apply_to_grid_horizontal(grid)
		elif include_diagonals and self.is_diagonal():
			grid = self.apply_to_grid_diagonal(grid)
		return grid

	def print_coords(self):
		print('{}, {} to {}, {}'.format(self.x_start, self.y_start, self.x_end, self.y_end))


def process_input(input_file):
	lines = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=' ')
		for row in csv_reader:
			line = Line(row[0], row[-1])
			lines.append(line)
	return lines


def count_danger_spots(grid, danger_threshold):
	result = 0
	for x in grid:
		for y in x:
			if y >= danger_threshold:
				result += 1
	return result


lines = process_input('input.csv')
grid_size = max(line.max for line in lines) + 1

grid = np.zeros((grid_size, grid_size))
for line in lines:
	grid = line.apply_to_grid(grid, False)
print('Danger spots part 1: {}'.format(count_danger_spots(grid, 2)))

grid = np.zeros((grid_size, grid_size))
for line in lines:
	grid = line.apply_to_grid(grid, True)
print('Danger spots part 2: {}'.format(count_danger_spots(grid, 2)))


