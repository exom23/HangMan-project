def ask_user_for_next_letter():
	letter = input("Guess your letter: ")
	return letter.strip().upper()


def generate_word_string(word, letters_guessed):
	output = []
	for letter in word:
		if letter in letters_guessed:
			output.append(letter.upper())
		else:
			output.append("_")
	return " ".join(output)
