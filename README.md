# Python Hangman using Webster's Dictionary
![My image](https://github.com/bgriessbach/pythonHangman/blob/master/screenshot.PNG)  
  
## Gameplay
+ Select the length of the word
+ the Webster Dictionary clue gets displayed
+ enter letters one by one or type "exit" to stop the game
+ if the letter does not occur or has already been found, you lose one try
+ if a new letter is found, the display updates
+ the game ends if all letters are found, or if you have entered 10+ wrong letters

![My image](https://github.com/bgriessbach/pythonHangman/blob/master/lost.PNG)

![My image](https://github.com/bgriessbach/pythonHangman/blob/master/won.PNG)  

## Progress
+ finished base of Game
+ added first Ascii Art
+ added Hangman Animation
+ added more Ascii art for End of Game
+ added check for multi-character input
+ Deleted the target word from the clue
+ hard coded window size and text color
+ found issues with source dictionary
  + some spaces missing
  + ~~some clues are only off target word by 1/2 letters~~ **Addressed**
+ User can type **Exit** to end the game
+ exclude words that have "see XXX" clues

