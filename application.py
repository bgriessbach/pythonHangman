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
print("A {} letter word will be selected.".format(wordLength))

#choose a random word
wordFound=wordTarget=d.decideWord(lengthWords[wordLength])
wrongLetters=0

#inialise and show word display
display=g.initialiseDisplay(wordTarget)
print(display)

#show Hangman


#ask for letter
letter=input("Choose a letter:")


#if letter in wordFound
#update display and wordFound
#else increment wrongLetter and update hangman
#check if game is won or max wrongLetters reached
#close game if won or lost





