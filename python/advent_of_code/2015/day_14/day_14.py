import input

def calculate_distance(speed, fly_time, rest_time, seconds):
	distance = int(seconds / (fly_time + rest_time)) * (speed * fly_time)
	remainder = seconds % (fly_time + rest_time)
	time_in_flight = 0
	while time_in_flight < fly_time and time_in_flight < remainder:
		distance += speed
		time_in_flight += 1
	return distance

def race_deer(puzzle_input, seconds, positions):
	deer = puzzle_input.split('\n')
	longest_distance = 0
	winner = ''
	for d in deer:
		reindeer, speed, fly_time, rest_time = process_input(d)
		distance = calculate_distance(speed, fly_time, rest_time, seconds)
		if distance > longest_distance:
			longest_distance = distance
			winner = reindeer
		if reindeer in positions:
			positions[reindeer] += distance
		else:
			positions[reindeer] = distance
	return longest_distance, positions

#doesn't work because they're starting at beginning each time
def race_deer_part_2(puzzle_input, seconds, positions):
	leaderboard = {}
	s = 1
	while s <= seconds:
		longest_distance, positions = race_deer(puzzle_input, 1, positions)
		winner = max(positions, key=positions.get)
		print(winner)
		s += 1

def process_input(deer_data):
	data = deer_data.split(' ')
	reindeer = data[0]
	speed = int(data[3])
	fly_time = int(data[6])
	rest_time = int(data[-2])
	return reindeer, speed, fly_time, rest_time

#print(race_deer(input.puzzle_input, 2503, {}))

print(race_deer_part_2(input.puzzle_input, 50, {}))