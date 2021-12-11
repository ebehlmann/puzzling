import csv
import numpy as np


def process_input(input_file):
	result = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			data = list(map(int, row[0]))
			result.append(data)
	return result

def get_surrounding(heightmap, x, y):
	surrounding = []
	if x > 0:
		surrounding.append(heightmap[x-1][y])
	if y > 0:
		surrounding.append(heightmap[x][y-1])
	if x < heightmap.shape[0]-1:
		surrounding.append(heightmap[x+1][y])
	if y < heightmap.shape[1]-1:
		surrounding.append(heightmap[x][y+1])
	return surrounding


def process_heightmap(heightmap):
	low_points = []
	x = 0
	y = 0
	while x < heightmap.shape[0]:
		while y < heightmap.shape[1]:
			surrounding = get_surrounding(heightmap, x, y)
			if heightmap[x][y] < min(surrounding):
				low_points.append(heightmap[x][y])
			y += 1
		x += 1
		y = 0
	return low_points


def calculate_risk_level(low_points):
	return sum(list(map(lambda x : x + 1, low_points)))

data = process_input('input.csv')
heightmap = np.array(data)
low_points = process_heightmap(heightmap)
risk_level = calculate_risk_level(low_points)
print(risk_level)


