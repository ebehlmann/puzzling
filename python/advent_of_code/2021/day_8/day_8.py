import csv

segment_lookup = {
	0: ['a', 'b', 'c', 'e', 'f', 'g'],
	1: ['c', 'f'],
	2: ['a', 'c', 'd', 'e', 'g'],
	3: ['a', 'c', 'd', 'f', 'g'],
	4: ['b', 'c', 'd', 'f'],
	5: ['a', 'b', 'd', 'f', 'g'],
	6: ['a', 'b', 'd', 'e', 'f', 'g'],
	7: ['a', 'c', 'f'],
	8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
	9: ['a', 'b', 'c', 'd', 'f', 'g']
}


def process_input(input_file):
	result = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			data = row[0].split('|')
			record = {
				'signal_pattern': data[0].split(),
				'output_values': data[1].split()
			}
			result.append(record)
	return result


def count_possible_outputs(notes, segment_data, digit):
	segments = len(segment_data[digit])
	result = 0
	for note in notes:
		for output in note['output_values']:
			if len(output) == segments:
				result += 1
	return result


def count_easy_digits(notes, segment_data):
	result = count_possible_outputs(notes, segment_data, 1)
	result += count_possible_outputs(notes, segment_data, 4)
	result += count_possible_outputs(notes, segment_data, 7)
	result += count_possible_outputs(notes, segment_data, 8)
	return result 


def count_appearances(signal_pattern):
	appearances = {}
	for signal in signal_pattern:
		for wire in signal:
			if wire in appearances:
				appearances[wire] += 1
			else:
				appearances[wire] = 1
	return appearances


def get_wire_by_count(appearances, count):
	result = []
	for k, v in appearances.items():
		if v == count:
			result.append(k)
	return result


def get_signal_by_length(signal_pattern, length):
	return [x for x in signal_pattern if len(x) == length]


def map_wires(signal_pattern):
	result = {}
	appearances = count_appearances(signal_pattern)
	
	result[get_wire_by_count(appearances, 6)[0]] = 'b'
	result[get_wire_by_count(appearances, 4)[0]] = 'e'
	result[get_wire_by_count(appearances, 9)[0]] = 'f'
	
	ac = get_wire_by_count(appearances, 8)
	for wire in ac:
		if wire in get_signal_by_length(signal_pattern, 2)[0]:
			result[wire] = 'c'
		else:
			result[wire] = 'a'

	dg = get_wire_by_count(appearances, 7)
	for wire in dg:
		if wire in get_signal_by_length(signal_pattern, 4)[0]:
			result[wire] = 'd'
		else:
			result[wire] = 'g'
	
	return result


def decode_digit(digit, signal_map):
	result = []
	for i in digit:
		result.append(signal_map[i])
	return result


def map_digits(signal_pattern, signal_map, segment_lookup):
	result = {}
	for digit in signal_pattern:
		decoded = decode_digit(digit, signal_map)
		for k, v in segment_lookup.items():
			if set(decoded) == set(v):
				result[''.join(sorted(digit))] = k
				break
	return result


def process_record(record, segment_lookup):
	signal_map = map_wires(record['signal_pattern'])
	digits = map_digits(record['signal_pattern'], signal_map, segment_lookup)
	result = ''
	for digit in record['output_values']:
		sorted_digit = ''.join(sorted(digit))
		result += str(digits[sorted_digit])
	return int(result)


notes = process_input('input.csv')

print('Easy digit count: {}'.format(count_easy_digits(notes, segment_lookup)))

sum = 0
for record in notes:
	sum += process_record(record, segment_lookup)
print('Sum of outputs: {}'.format(sum))








