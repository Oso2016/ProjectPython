# Name:
# Date:


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

#your code begins here!
def hangman():
    string_list = []
    blank_list = []
    word = choose_word(wordlist)
    guess = 6
    alphabet = string.lowercase
    length = len(word)
    print "I picked a word that is " + str(length) + " letters long."
    print alphabet
    for letter in word:
        string_list.append(letter)
        blank_list.append("_")




    while guess > 0:
        guess_input = raw_input("Guess a letter: ")
        guess -= 1





        for num in range(len(string_list)):
            if string_list[num] == guess_input:
                guess += 1
                blank_list[num] = guess_input
        if blank_list == string_list:
                print "You win!! :) "
                print string_list
                break

        print blank_list
        if guess == 5:
            print "You have 5 guesses left."
        if guess == 4:
            print "You have 4 guesses left."
        if guess == 3:
            print "You have 3 guesses left."
        if guess == 2:
            print "You have 2 guesses left."
        if guess == 1:
            print "You have 1 guess left."

    if guess == 0:
        print "Game over. Play again."
        print string_list









    return word

hangman()
