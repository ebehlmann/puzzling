import input
from itertools import permutations

def process_input(puzzle_input):
	data = puzzle_input.split('\n')
	cities = []
	processed = {}
	for datum in data:
		datum = datum.split(' ')
		processed[datum[0] + ' to ' + datum[2]] = int(datum[-1])
		if datum[0] not in cities:
			cities.append(datum[0])
		if datum[2] not in cities:
			cities.append(datum[2])
	return cities, processed

def calculate_route(route, data):
	distance = 0
	i = 0
	while i < len(route)-1:
		departing = route[i]
		arriving = route[i+1]
		key = departing + ' to ' + arriving
		if key in data:
			distance += data[key]
		else: 
			distance += data[arriving + ' to ' + departing]
		i += 1
	return distance

def find_route(cities, data):
	options = permutations(cities)
	shortest_distance = calculate_route(cities, data)
	longest_distance = 0
	for option in options:
		distance = calculate_route(option, data)
		if distance < shortest_distance:
			shortest_distance = distance
		if distance > longest_distance:
			longest_distance = distance
	return shortest_distance, longest_distance


cities, processed_input = process_input(input.puzzle_input)

shortest, longest = find_route(cities, processed_input)

print(shortest)
print(longest)