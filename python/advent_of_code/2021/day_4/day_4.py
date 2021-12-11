import csv


class Board():
	def __init__(self, layout):
		self.has_won = False
		self.layout = layout
		self.row_size = 5
		#self.marks = [[0] * self.row_size] * self.row_size
		self.marks = [[0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0]
		]

	def mark_board(self, number):
		i = 0
		j = 0
		while i < len(self.layout):
			while j < len(self.layout[i]):
				if self.layout[i][j] == number:
					self.marks[i][j] = 1
				j += 1
			i += 1
			j = 0

	def is_winner(self):
		if self.is_vertical_winner() or self.is_horizontal_winner():
			return True
		return False

	def is_horizontal_winner(self):
		for row in self.marks:
			if sum(row) == self.row_size:
				return True
		return False

	def is_vertical_winner(self):
		i = 0
		while i < self.row_size:
			sum = 0
			for row in self.marks:
				sum += row[i]
				if sum == self.row_size:
					return True
			i += 1
		return False

	def calculate_score(self, number_just_called):
		i = 0
		j = 0
		sum = 0
		while i < self.row_size:
			while j < self.row_size:
				if self.marks[i][j] == 0:
					sum += self.layout[i][j]
				j += 1
			i += 1
			j = 0
		return sum * number_just_called


def process_input(input_file):
	layouts = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		call_numbers = list(map(int, next(csv_reader)))
		layout = []
		for row in csv_reader:
			if len(row) == 0:
				if len(layout) > 0: 
					layouts.append(layout)
					layout = []
			else:
				layout.append(list(map(int, row[0].split())))
		layouts.append(layout)
	return call_numbers, layouts


def run_bingo(boards, call_numbers):
	scores = []
	for number in call_numbers:
		print('Next number is: {}'.format(number))
		for board in boards:
			board.mark_board(number)
			if board.is_winner():
				if board.has_won == False:
					score = board.calculate_score(number)
					print('BINGO!!! Score: {}'.format(score))
					board.has_won = True
					scores.append(score)
	return scores
				
			

call_numbers, layouts = process_input('input.csv')

boards = []
for layout in layouts:
	board = Board(layout)
	boards.append(board)

scores = run_bingo(boards, call_numbers)
print('First winner score: {}'.format(scores[0]))
print('Last winner score: {}'.format(scores[-1]))