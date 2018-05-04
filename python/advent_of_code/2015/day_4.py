import hashlib

def zeroes_check(test_hash, zeroes_needed):
	i = 0
	while i < zeroes_needed:
		if test_hash[i] != '0':
			return False
		i+=1
	return True

def find_hash(puzzle_input, zeroes_needed):
	num = 1
	while True:
		h = hashlib.md5(puzzle_input + str(num)).hexdigest()
		if zeroes_check(h, zeroes_needed) == True:
			break
		else: 
			num += 1
	return num

print(find_hash('bgvyzdsv', 5))
print(find_hash('bgvyzdsv', 6))