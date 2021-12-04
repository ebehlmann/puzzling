import csv
import abc


class Calibrator(abc.ABC):
	def __init__(self):
		self.horizontal = 0
		self.depth = 0

	def process_input(self, input_file):
		with open(input_file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				instruction = row[0].split()[0]
				amount = int(row[0].split()[1])
				position = self.adjust_position(instruction, amount)	

	def adjust_position(self, instruction, amount):
		pass


class PositionCalibratorSimple(Calibrator):
	def __init__(self):
		super().__init__()

	def adjust_position(self, instruction, amount):
		if instruction == 'up':
			self.depth -= amount
		elif instruction == 'down':
			self.depth += amount
		else:
			self.horizontal += amount


class PositionCalibratorComplex(Calibrator):
	def __init__(self):
		super().__init__()
		self.aim = 0

	def adjust_position(self, instruction, amount):
		if instruction == 'up':
			self.aim -= amount
		elif instruction == 'down':
			self.aim += amount
		else:
			self.horizontal += amount
			self.depth += (amount * self.aim)


calibrator = PositionCalibratorSimple()
calibrator.process_input('input.csv')
print('Part 1: {}'.format(calibrator.horizontal * calibrator.depth))

calibrator = PositionCalibratorComplex()
result = calibrator.process_input('input.csv')
print('Part 2: {}'.format(calibrator.horizontal * calibrator.depth))


