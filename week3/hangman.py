
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord_array = list(secretWord)
    
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in secretWord_array:
            secretWord_array.remove(lettersGuessed[i])
    
    if secretWord_array == []:
        return True
    else: 
        return False
            

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord_array = ["_ "] * len(secretWord)
    
    for i in range(len(lettersGuessed)):
        for j in range(len(secretWord)):
            if lettersGuessed[i] == secretWord[j]:
                secretWord_array[j] = lettersGuessed[i]
    
    guessed_word = ''.join(secretWord_array)
    return guessed_word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Convert to array as strings are immutable 
    available_letters_array = list(string.ascii_lowercase)
    
    for i in range(len(lettersGuessed)): 
        if lettersGuessed[i] in available_letters_array:
            available_letters_array.remove(lettersGuessed[i])
    
    return "".join(available_letters_array)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman.
    '''
    
    user_guesses = []
    num_guesses = 0
    
    print "The word contains " + str(len(secretWord)) + " letters"
    
    while num_guesses < 8:
        print "*****************"
        print "You have " + str(8 - num_guesses) + " guesses left"
        print "Available letters: " + str(getAvailableLetters(user_guesses))
        
        user_guess = raw_input("Please guess a letter: ").lower()
        
        if user_guess in user_guesses:
            print "Oops you have already guessed that letter: " + str(getGuessedWord(secretWord, user_guesses))
        
        else:
            user_guesses.append(user_guess)
            num_guesses += 1
                
            if user_guess in secretWord:
                print "Good guess: " + str(getGuessedWord(secretWord, user_guesses))
                
                if isWordGuessed(secretWord, user_guesses):
                    print "*****************"
                    print "Congratulations, you've guessed my word!"
                    return                    
            
            else:
                print "Sorry, that letter is not in my word: " + str(getGuessedWord(secretWord, user_guesses))
                if num_guesses == 8:
                    print "*****************"
                    print "Sorry, you are out of guesses, the word was: " + secretWord
                    
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
