# Write a recursive function for generating all permutations of an input string. Return them as a set.

def get_string_permutation(word):
	if len(word) == 2:
		results = set()
		permutation = [word[0]]
		i = 0
		while i < len(word):
			permutation.insert(i, word[1])
			results.add(''.join(permutation))
			i += 1
			permutation = [word[0]]
	else:
		results = set()
		
	return results


print(get_string_permutation('hi'))