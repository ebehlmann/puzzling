def find_small_enough(containers, amount):
	small_enough = []
	for container in containers:
		if container < amount:
			small_enough.append(container)
	return small_enough

# def find_combinations(containers, amount):
# 	containers = sorted(containers, reverse=True)
# 	combinations = []
# 	total = 0
# 	for container in containers:
# 		permutation = []
# 		permutation.append(container)
# 		total += container
# 		while total <= amount:
# 			remaining = find_small_enough(containers, (amount-total))



#containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47, 36, 24, 22, 40]
containers = [5, 20, 15, 10, 5]
print(find_combinations(containers, 25))

#print(find_permutations(150, containers))