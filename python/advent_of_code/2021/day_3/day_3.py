import csv
from collections import Counter


def process_input(input_file):
	binaries = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			binaries.append(row[0])
	return binaries


def find_most_common_for_bit(binaries, index):
	bits = []
	for binary in binaries:
		bits.append(binary[index])
	occurence_count = Counter(bits)
	# in case of a tie return 1
	if occurence_count.most_common(2)[0][1] == occurence_count.most_common(2)[1][1]:
		return 1
	return occurence_count.most_common(1)[0][0]


def get_gamma_string(binaries):
	gamma = ''
	i = 0
	while i < len(binaries[0]):
		gamma += find_most_common_for_bit(binaries, i)
		i += 1
	return gamma


def get_epsilon_string(gamma):
	epsilon = ''
	for i in range(0, len(gamma)):
		epsilon += str(abs(int(gamma[i]) - 1))
	return epsilon


def multiply_binaries(one, two):
	return int(one, 2) * int(two, 2)


def get_rating(binaries, type):
	i = 0
	while i < len(binaries[0]):
		value = str(find_most_common_for_bit(binaries, i))
		if type == 'co2':
			value = str(abs(int(value) - 1))
		binaries = list(filter(lambda x: x[i] == value, binaries))
		if len(binaries) == 1:
			break
		i += 1
	return binaries[0]


binaries = process_input('input.csv')

gamma = get_gamma_string(binaries)
epsilon = get_epsilon_string(gamma)
power_consumption = multiply_binaries(gamma, epsilon)
print('Power consumption: {}'.format(power_consumption))

oxygen_generator_rating = get_rating(binaries, 'oxygen')
co2_scrubber_rating = get_rating(binaries, 'co2')
life_support_rating = multiply_binaries(oxygen_generator_rating, co2_scrubber_rating)
print('Life support rating: {}'.format(life_support_rating))

