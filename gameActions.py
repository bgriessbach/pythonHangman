def initialiseDisplay(word):
	display=""
	for letter in word:
		if letter.isalpha():
			display+="_ "
		else:
			display+=letter
	return display



