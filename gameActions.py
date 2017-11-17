#setup display first time
#letters should be shown as "_"
#non-letters like " " or "-" should be displayed
def initialiseDisplay(word):
	display=[]
	for letter in word:
		if letter.isalpha():
			display.append("_")
		else:
			display.append(letter)
	print(" ".join(display)+"\n\n")
	return display

#query user for input
#if input is not a letter, repeat prompt
def letterInput():
	myinput=""
	while myinput.isalpha()!=True:
		myinput=input("Choose a letter:")
	return myinput.upper()

#check if game ends
#game ends if no "_" remain or too many wrong tries
def gameEnd(display, tries):
	if tries>10:
		return True
	if "_" not in display:
		return True
	return False

#when letter is found
#update display to reflect new letter
def updateDisplay(display, letter, mydict):
	index=mydict[letter]
	while len(index)>0:
		display[index.pop()]=letter
	print(" ".join(display)+"\n\n")
	return display



