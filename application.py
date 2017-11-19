import dictionary as d
import gameActions as g
import os


#load dictionaries
lengthWords,wordsWebster=d.loadWords()

#set window color and size
os.system("Color 75")
os.system("mode con cols=90 lines=40")



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
print("Welcome to Hangman using Webster's Dictionary:\n\n")
wordLength=0
while wordLength<4 or wordLength>45:
	userInput=input("How many letters?(4-45)")
	if userInput.isdigit():
		wordLength=int(userInput)
print("We have selected a {} letter word.".format(wordLength))

#choose a random word
wordTarget=d.decideWord(lengthWords[wordLength])
#create dictionary for letter indexes of chosen word
letterIndex=d.createLetterIndex(wordTarget)
#set wrong tries
wrongLetters=0

#clean clue
clue=d.cleanClue(wordTarget, wordsWebster[wordTarget])

print("Clue: {}".format(clue))

#inialise and show word display
display=g.initialiseDisplay(wordTarget)

#check if game is won
#otherwise query for input and evaluate input
while g.gameEnd(display, wrongLetters)!=True:
	letter=g.letterInput()
	if letter in display:
		print("Letter {} already used.".format(letter.upper()))
		wrongLetters+=1
		g.animationHangman(wrongLetters)
		print(" ".join(display)+"\n\n")
	elif letter not in wordTarget:
		print("Letter {} not found.".format(letter.upper()))
		wrongLetters+=1
		g.animationHangman(wrongLetters)
		print(" ".join(display)+"\n\n")
	else:
		print("Letter found.")
		display=g.updateDisplay(display, letter, letterIndex)


#End Game either in Loss or Success
if wrongLetters>9:
	print('''

 __     __           _           _     _   _                                        
 \ \   / /          | |         | |   | | | |                                       
  \ \_/ ___  _   _  | | ___  ___| |_  | |_| |__   ___    __ _  __ _ _ __ ___   ___  
   \   / _ \| | | | | |/ _ \/ __| __| | __| '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \ 
    | | (_) | |_| | | | (_) \__ | |_  | |_| | | |  __/ | (_| | (_| | | | | | |  __/ 
    |_|\___/ \__,_| |_|\___/|___/\__|  \__|_| |_|\___|  \__, |\__,_|_| |_| |_|\___| 
                                                         __/ |                      
                                                        |___/                       
                                                                                    



		''')
else:
	print('''


   _____                            _         _       _   _                  
  / ____|                          | |       | |     | | (_)                 
 | |     ___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_ _  ___  _ __  ___  
 | |    / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| 
 | |___| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \ 
  \_____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/ 
                     __/ |                                                   
                    |___/                                                    
                                                                             
                                                                             
	''')
	print("{} : {}".format(wordTarget, wordsWebster[wordTarget]))



