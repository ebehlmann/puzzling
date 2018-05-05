import input

# combining these into one function to avoid iterating over the string twice
def check_for_vowels_and_doubles(s, vowel_min):
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowel_count = 0
	doubles = False
	i = 0
	while i < len(s):
		if s[i] in vowels:
			vowel_count += 1
		if i < len(s) - 1 and s[i] == s[i+1]:
			doubles = True
		i += 1
	if vowel_count >= vowel_min and doubles == True:
		return True
	return False

def check_for_bad_strings(s, bad_list):
	for bad in bad_list:
		if bad in s:
			return True
	return False

def check_for_repeating_pair(s):
	i = 0
	while i < len(s)-1:
		pair = s[i:i+2]
		j = i + 2
		while j < len(s)-1:
			test_pair = s[j:j+2]
			if pair == test_pair:
				return True
			j += 1
		i += 1
	return False

def check_for_repeating_letter(s):
	i = 0
	while i < len(s)-2:
		if s[i] == s[i+2]:
			return True
		i += 1
	return False

def is_nice_part_one(s, bad_list, vowel_min):
	if check_for_bad_strings(s, bad_list) == True:
		return False
	elif check_for_vowels_and_doubles(s, vowel_min) == True:
		return True
	return False

def is_nice_part_two(s):
	if check_for_repeating_pair(s) == True and check_for_repeating_letter(s) == True:
		return True
	return False

def nice_counts(strings):
	part_1 = 0
	part_2 = 0
	for s in strings:
		if is_nice_part_one(s, ['ab', 'cd', 'pq', 'xy'], 3) == True:
			part_1 += 1
		if is_nice_part_two(s) == True:
			part_2 += 1
	return part_1, part_2

strings = input.puzzle_input.split('\n')
part_1, part_2 = nice_counts(strings)
print(part_1)
print(part_2)