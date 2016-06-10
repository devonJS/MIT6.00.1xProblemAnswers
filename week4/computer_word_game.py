from ps4a import *
import time

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    comp_max_score = 0
    comp_best_word = ''
    
    for i in range(len(wordList)):
        if isValidWord(wordList[i], hand, wordList):
            word_score = getWordScore(wordList[i], n)
            if word_score > comp_max_score:
                comp_max_score = word_score
                comp_best_word = wordList[i]

    if comp_max_score == 0:
        return None
        
    return comp_best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    comp_total_score = 0
    
    while calculateHandlen(hand) > 0:
        print "Current hand: "
        displayHand(hand)
        comp_word_choice = compChooseWord(hand, wordList, n)
        
        if comp_word_choice == None:
            print "Total score: " + str(comp_total_score) + " points."
            break
            
        comp_word_score = getWordScore(comp_word_choice, n)
        comp_total_score += comp_word_score
        hand = updateHand(hand, comp_word_choice)
        print '"' + comp_word_choice + '"' + ' earned ' + str(comp_word_score) + ' points.' + " Total: " + str(comp_total_score) + " points."

#
# Problem #8: Playing a game
#
#
global comp_current_hand
comp_current_hand = {}

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    global comp_current_hand
    
    hand_option_input = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    mode_selection = False
    
    if hand_option_input == 'n' or hand_option_input == 'r':
        mode_selected = False
        
        if hand_option_input == 'n':
            comp_current_hand = dealHand(HAND_SIZE)
            
        elif hand_option_input == 'r' and not comp_current_hand:
            print "You have not played a hand yet. Please play a new hand first!"
            playGame(wordList)
                
        while not mode_selected:
            mode_option_input = raw_input("Enter u to have yourself play, c to have the computer play: ")
            
            if mode_option_input == 'u':
                playHand(comp_current_hand, wordList, HAND_SIZE)
                mode_selected = True
                playGame(wordList)
            elif mode_option_input == 'c':
                compPlayHand(comp_current_hand, wordList, HAND_SIZE)
                mode_selected = True
                playGame(wordList)
            else:
                print "Invalid command."
    elif hand_option_input == 'e':
        print "See ya"
        mode_selected = True
        return
    else:
        print "Invalid command."
        playGame(wordList)

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


