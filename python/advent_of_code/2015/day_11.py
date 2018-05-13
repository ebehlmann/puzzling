def increment_password(password, digit):
	pass_as_list = list(password)
	if ord(pass_as_list[digit]) == 122:
		pass_as_list[digit] = chr(97)
		password = increment_password(''.join(pass_as_list), digit-1)
	else:
		pass_as_list[digit] = chr(ord(pass_as_list[digit])+1)
		password = ''.join(pass_as_list)
	return password

def check_for_sequence(password):
	i = 0
	while i < len(password) - 2:
		if ord(password[i]) - ord(password[i+1]) == -1:
			if ord(password[i+1]) - ord(password[i+2]) == -1:
				return True
		i += 1
	return False

def check_for_doubles(password):
	doubles = 0
	i = 0
	while i < len(password) - 1:
		if password[i] == password[i+1]:
			doubles += 1
			if doubles == 2:
				return True
			i += 2
		else:
			i += 1
	return False

def check_for_forbidden_chars(password, forbidden):
	for c in forbidden:
		if c in password:
			return True
	return False

def find_next_password(password):
	while True:
		password = increment_password(password, -1)
		if check_for_forbidden_chars(password, ['i', 'o', 'l']) == False: 
			if check_for_sequence(password) == True and check_for_doubles(password) == True:
				break
	return password


part_1 = find_next_password('cqjxjnds')
part_2 = find_next_password(part_1)

print(part_1)
print(part_2)