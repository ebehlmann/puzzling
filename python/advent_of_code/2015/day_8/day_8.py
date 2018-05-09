def process_string(s):
	length = 0
	s = s[1:-1]
	i = 0
	while i < len(s):
		if s[i] == '\\':
			if i + 3 <= len(s) and s[i+1] == 'x':
				i += 4
			elif i + 1 <= len(s) and (s[i+1] == '\\' or s[i+1] == '"'):
				i += 2
		else: 
			i += 1
		length += 1
	return length

def find_diff(file):
	literals = 0
	chars_in_memory = 0
	for line in open(file):
		literals += len(line)
		chars_in_memory += process_string(line)
	return literals-chars_in_memory

print(find_diff('input.txt'))
