import random

def pick_random_word():
	"""
	This function picks a random word from the SOWPODS
	dictionary. 
	"""
	# open the sowpods dictionary
	with open("sowpods.txt", 'r') as f:
		words = f.readlines()

	# generate a random index
	# -1 because len(words) is not a valid index into the list `words`
	index = random.randint(0, len(words) - 1)

	# print out the word at that index
	word = words[index].strip()
	return word
