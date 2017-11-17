import dictionary as d
import gameActions as g


#load dictionaries
lengthWords,wordsWebster=d.loadWords()

#print welcome message and ask user for prefered word length
#only allow int input >3 and <46
#repeat input prompt until valid input found
print('''

  _    _                                                
 | |  | |                                               
 | |__| |  __ _  _ __    __ _  _ __ ___    __ _  _ __   
 |  __  | / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \  
 | |  | || (_| || | | || (_| || | | | | || (_| || | | | 
 |_|  |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_| 
                         __/ |                          
                        |___/                           

	''')
print("Welcome to Hangman using Webster Dictionary:\n\n")
wordLength=0
while wordLength<4 or wordLength>45:
	userInput=input("How many letters?(4-45)")
	if userInput.isdigit():
		wordLength=int(userInput)
print("We will select a {} letter word.".format(wordLength))

#choose a random word
wordTarget=d.decideWord(lengthWords[wordLength])
#create dictionary for letter indexes of chosen word
letterIndex=d.createLetterIndex(wordTarget)
#set wrong tries
wrongLetters=0
print("Clue: {}".format(wordsWebster[wordTarget]))

#inialise and show word display
display=g.initialiseDisplay(wordTarget)


#show Hangman

#check if game is won
#otherwise query for input and evaluate input
while g.gameEnd(display, wrongLetters)!=True:
	letter=g.letterInput()
	if letter in display:
		print("Letter already found. Hangman grows.")
		wrongLetters+=1
	elif letter not in wordTarget:
		print("Letter not found. Hangman grows.")
		wrongLetters+=1
	else:
		print("Letter found.")
		display=g.updateDisplay(display, letter, letterIndex)
	#g.displayHangman(wrongLetters)

if wrongLetters>10:
	print("You lost the game.")
else:
	print("Congratulations.\n{} : {}".format(wordTarget, wordsWebster[wordTarget]))



#ask for letter





#if letter in wordFound
#update display and wordFound
#else increment wrongLetter and update hangman
#check if game is won or max wrongLetters reached
#close game if won or lost





