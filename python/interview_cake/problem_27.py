"""
Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in-place.
"""

#this is a mess

def reverse_words(message):
	stop = len(message)
	current_word = []
	i = 0
	while i < stop:
		char = message.pop()
		if char != ' ':
			current_word.insert(0, char)
		else: 
			j = 0
			while j < len(current_word):
				message.append(current_word[j])
				print(message)
				j += 1
			current_word = []
		i += 1
	print(current_word)

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)
#print(message)

# Prints: 'steal pound cake'
#print ''.join(message)