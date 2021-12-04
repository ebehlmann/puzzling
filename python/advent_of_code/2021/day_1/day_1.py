import csv


def convert_input(input_file):
	data = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			data.append(int(row[0]))
	return data


def count_increases(input_array):
	increases = 0
	depth = input_array[0]
	for reading in input_array[1:]:
		if reading > depth:
			increases += 1
		depth = reading
	return increases


def count_increases_sliding_window(input_array, window_size):
	increases = 0
	start = 0
	end = start + window_size
	depth = sum(input_array[start:end])
	while len(input_array) > end-1:
		new_depth = sum(input_array[start:end])
		if new_depth > depth:
			increases += 1
		depth = new_depth
		start += 1
		end += 1
	return increases


data = convert_input('input.csv')

part_1 = count_increases(data)
print('Part 1: {}'.format(part_1))

part_2 = count_increases_sliding_window(data, 3)
print('Part 2: {}'.format(part_2))