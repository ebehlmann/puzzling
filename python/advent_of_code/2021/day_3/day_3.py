import csv
from collections import Counter


def process_input(input_file):
	binaries = []
	with open(input_file) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			binaries.append(row[0])
	return binaries


def get_gamma_string(binaries):
	gamma = ''
	i = 0
	while i < len(binaries[0]):
		bits = []
		for binary in binaries:
			bits.append(binary[i])
		i += 1
		occurence_count = Counter(bits)
		gamma += occurence_count.most_common(1)[0][0]
	return gamma


def get_epsilon_string(gamma):
	epsilon = ''
	for i in range(0, len(gamma)):
		epsilon += str(abs(int(gamma[i]) - 1))
	return epsilon


def calculate_power_consumption(gamma, epsilon):
	return int(gamma, 2) * int(epsilon, 2)


binaries = process_input('input.csv')
gamma = get_gamma_string(binaries)
epsilon = get_epsilon_string(gamma)
power_consumption = calculate_power_consumption(gamma, epsilon)
print(power_consumption)