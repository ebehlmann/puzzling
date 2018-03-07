"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.
Each order is represented by an "order id" (an integer).
We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
"""

# def merge_lists(list1, list2):
# 	merged = list1 + list2
# 	merged.sort()
# 	return merged

# runs slightly faster than relying on built-in sorting functions
# (0.030 seconds vs 0.037 seconds)
def merge_lists(list1, list2):
	merged = []
	i = 0
	j = 0

	while len(merged) < len(list1) + len(list2):
		if len(list1) > i:
			el1 = list1[i]
		else:
			el1 = el2+1

		if len(list2) > j:	
			el2 = list2[j]
		else:
			el2 = el1+1

		if el1 < el2:
			merged.append(el1)
			i += 1
		else:
			merged.append(el2)
			j += 1

	return merged

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)