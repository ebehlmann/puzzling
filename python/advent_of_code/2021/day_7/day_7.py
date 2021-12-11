import input


def calculate_fuel_cost_1(crabs, position):
	fuel = 0
	for c in crabs:
		fuel += abs(position - c)
	return fuel


def calculate_fuel_cost_2(crabs, position):
	fuel = 0
	for c in crabs:
		distance = abs(position - c)
		if distance > 0:
			fuel += sum(list(range(1, distance + 1)))
	return fuel


def find_optimal_position(crabs, method):
	fuel = float('inf')
	pos = min(crabs)
	max_pos = max(crabs)
	while pos <= max_pos:
		if method == 1:
			fuel_pos = calculate_fuel_cost_1(crabs, pos)
		else:
			fuel_pos = calculate_fuel_cost_2(crabs, pos)
		if fuel_pos < fuel:
			fuel = fuel_pos
		pos += 1
	return fuel


crabs = input.crabs
print(find_optimal_position(crabs, 1))
print(find_optimal_position(crabs, 2))
