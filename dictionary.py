import json
import os, sys
import random as r

#Load words from the Webster JSON file
#return 1 dictonary with length:[words] structure
#return 1 dictionary with words:meaning structure

def loadWords():
	lengthDict={}
	try:
		fileName=os.path.dirname(sys.argv[0])+"\\"+"words_dictionary.json"
		with open(fileName, "r") as englishDict:
			validWords=json.load(englishDict)
	except Exception as e:
		return str(e)
	for item in validWords.keys():
		length=len(item)
		if length in lengthDict.keys():
			lengthDict[length].append(item)
		else:
			lengthDict[length]=[item]
	return lengthDict, validWords


#decide a word from the list at random
#if the connect clue starts with "see", try again
def decideWord(wordList, clueList):
	listLength=len(wordList)
	index=-1
	while index<0:
		index=r.randrange(0,listLength)
		if clueList[wordList[index]][:3]=="see":
			index=-1
	return wordList[index]

#create an index dict
#it will have letters as keys and index references as values
#this improves update times for the game display
def createLetterIndex(word):
	mydict={}
	for index in range(len(word)):
		if word[index] in mydict.keys():
			mydict[word[index]].append(index)
		else:
			mydict[word[index]]=[index]
	return mydict


# clean the clue text so it does not show the Target Word or parts of the target word (4+ digits)
def cleanClue(word, clue):
	word=word.lower()
	clue=clue.lower()
	while len(word)>3:
		clue=clue.replace(word, "XXX")
		word=word[:-1]
	return clue

