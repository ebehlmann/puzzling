import csv
import math


def reduce_line(line):
	char_sets = ['()', '[]', '{}', '<>']
	while True:
		count = 0
		for char_set in char_sets:
			x = line.find(char_set)
			line = line.replace(char_set, '')
			count += x
		if count == -4:
			break
	return line


def find_illegal_char(reduced_line):
	legal_predecessors = {')': '(', ']': '[', '}': '{', '>': '<'}
	i = 0
	while i < len(reduced_line):
		if reduced_line[i] in legal_predecessors:
			if i == 0 or reduced_line[i-1] != legal_predecessors[reduced_line[i]]:
				return reduced_line[i]
		i += 1
	return None


def autocomplete_line(reduced_line):
	legal_closers = {'(': ')', '[': ']', '{': '}', '<': '>'}
	autocomplete = ''
	for c in reduced_line:
		autocomplete = legal_closers[c] + autocomplete
	return autocomplete


def calculate_auto_complete_score(autocomplete):
	lookup = {')': 1, ']': 2, '}': 3, '>': 4}
	score = 0
	for c in autocomplete:
		score = score * 5 + lookup[c]
	return score


def get_middle_score(scores):
	pos = math.floor(len(scores) / 2)
	return sorted(scores)[pos]


def calculate_scores(lines):
	error_score = 0
	error_score_lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
	
	autocomplete_scores = []
	
	for line in lines:
		reduced = reduce_line(line)
		if len(reduced) > 0:
			illegal = find_illegal_char(reduced)
			if illegal:
				error_score += error_score_lookup[illegal]
			else:
				autocomplete = autocomplete_line(reduced)
				autocomplete_scores.append(calculate_auto_complete_score(autocomplete))
	
	return error_score, get_middle_score(autocomplete_scores)


def process_input(input_file):
	lines = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			lines.append(row[0])
	return lines


lines = process_input('input.csv')
error_score, autocomplete_scores = calculate_scores(lines)
print('Error score: {}'.format(error_score))
print('Autocomplete score: {}'.format(autocomplete_scores))

