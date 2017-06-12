# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
computer_answer = random.randint(1,9)
guess = raw_input("Guess a number between 1 and 9:")
numberguesses = 3
if guess == "exit":
    print "Have a good day!"
else:
    guess = int(guess)
    while guess != computer_answer and numberguesses > 0:
        print "Sorry, wrong answer. Guess again."
        guess = raw_input("Guess a number between 1 and 9:")
        numberguesses = numberguesses -1
        if guess == computer_answer:
            print "Good Job! You guessed correctly!"
        if guess == "exit":
            print "Have a good day!"
            break



