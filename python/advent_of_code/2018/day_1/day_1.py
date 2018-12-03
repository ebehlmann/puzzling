import input

def calibrate(input, frequency):
	if input[0] == '+':
		frequency += int(input[1:])
	else:
		frequency -= int(input[1:])
	return frequency

def process_instructions(instructions, frequency):
	for i in instructions: 
		frequency = calibrate(i, frequency)
	return frequency

def find_repeat(input, frequency):
	frequencies = []
	while True:
		for i in instructions:
			frequency = calibrate(i, frequency)
			if frequency in frequencies:
				return frequency
			frequencies.append(frequency)

instructions = input.puzzle_input.split('\n')

print('Frequency after one round: ' + str(process_instructions(instructions, 0)))
print('First repeat: ' + str(find_repeat(instructions, 0)))