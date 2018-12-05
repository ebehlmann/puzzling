import input

def parse_claim(claim):
	claim_array = claim.split(' ')
	position = claim_array[2].split(',')
	size = claim_array[3].split('x')
	return claim_array[0][1:], int(position[0]), int(position[1][:-1]), int(size[0]), int(size[1])

def mark_claim(claim_id, position_x, position_y, size_x, size_y, fabric):
	y = position_y
	while y < position_y + size_y:
		x = position_x
		while x < position_x + size_x:
			key = str(x) + ', ' + str(y)
			if key in fabric:
				fabric[key].append(claim_id)
			else:
				fabric[key] = [claim_id]
			x += 1
		y += 1
	return fabric

def process_claims(claims):
	fabric = {}
	for claim in claims:
		claim_id, position_x, position_y, size_x, size_y = parse_claim(claim)
		fabric = mark_claim(claim_id, position_x, position_y, size_x, size_y, fabric)
	return fabric

def find_multiple_claims(fabric):
	multiples = 0
	claims_in_singles = []
	claims_in_multiples = []
	for i in fabric:
		if len(fabric[i]) > 1:
			multiples += 1
			for claim in fabric[i]:
				if claim not in claims_in_multiples:
					claims_in_multiples.append(claim)
		else:
			claim = fabric[i][0]
			if claim not in claims_in_singles:
				claims_in_singles.append(fabric[i][0])
	return multiples, claims_in_singles, claims_in_multiples

def find_non_overlapping_claim(claims_in_singles, claims_in_multiples):
	result = []
	for claim in claims_in_singles:
		if claim not in claims_in_multiples:
			result.append(claim)
	return result

claims = input.puzzle_input.split('\n')
fabric = process_claims(claims)
multiple_claims, claims_in_singles, claims_in_multiples = find_multiple_claims(fabric)
print(multiple_claims)
print(find_non_overlapping_claim(claims_in_singles, claims_in_multiples))