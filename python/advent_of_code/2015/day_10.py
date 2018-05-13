def look_and_say(number):
	num_as_string = str(number)
	i = 0
	count = 0
	result = ''
	digit = num_as_string[0]

	while i < len(num_as_string):
		if num_as_string[i] == digit:
			count += 1
		else:
			result += str(count)
			result += str(digit)
			count = 1
			digit = num_as_string[i]
		i += 1

	result += str(count)
	result += str(digit)
	return int(result)

def run_cycle(instances, starting_number):
	i = 1
	n = starting_number
	while i <= instances:
		print(i)
		n = look_and_say(n)
		i += 1
	return n

result = run_cycle(50, 1113222113)
print(len(str(result)))