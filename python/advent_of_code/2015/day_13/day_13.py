import input
from itertools import permutations

def process_input(input):
	notes = input.split('\n')
	guests = []
	result = {}
	for note in notes:
		note = note.split(' ')
		# build guest list
		if note[0] not in guests:
			guests.append(note[0])
		# set happiness change amount
		amount = int(note[3])
		if note[2] == 'lose':
			amount = amount * -1
		# add dictionary entry
		result[note[0] + '-' + note[-1][:-1]] = amount
	return guests, result


def calculate_happiness(arrangement, data):
	happiness = 0
	i = 0
	while i < len(arrangement):
		if i == len(arrangement) -1:
			next_to = 0
		else:
			next_to = i+1
		if arrangement[i] == 'me' or arrangement[next_to] == 'me':
			happiness += 0
		else:
			happiness += data[arrangement[i] + '-' + arrangement[next_to]]
			happiness += data[arrangement[next_to] + '-' + arrangement[i]]
		i += 1
	return happiness

def find_best_arrangement(guests, data):
	arrangements = permutations(guests)
	happiness = 0
	optimal = []
	for arrangement in arrangements:
		score = calculate_happiness(arrangement, data)
		if score > happiness:
			happiness = score
			optimal = arrangement
	return happiness, optimal

def insert_zero_score(optimal, data):
	i = 0
	happiness = 0
	while i <= len(optimal):
		arrangement = list(optimal)
		arrangement.insert(i, 'me')
		score = calculate_happiness(arrangement, data)
		if score > happiness:
			happiness = score
		i += 1
	return happiness

guests, data = process_input(input.puzzle_input)
happiness1, optimal1 = find_best_arrangement(guests, data)
print(optimal1)
print(happiness1)

guests.append('me')
happiness2, optimal2 = find_best_arrangement(guests, data)
print(optimal2)
print(happiness2)

print(happiness1-happiness2)


#with_me = insert_zero_score(optimal, data)
#print(with_me - happiness)