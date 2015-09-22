#http://www.codeskulptor.org/#user40_Hgg6y5Dzfd_3.py

import simplegui
import random
import math

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

secret_number = 0
range = 100
num_guesses = 0

# helper function to start and restart the game
def remaining_guesses():
    if range == 100:
        return 7 - num_guesses
    else:
        return 10 - num_guesses
    
def new_game():
    # initialize global variables used in your code here
    print
    global num_guesses
    num_guesses = 0
    global secret_number
    secret_number = random.randrange(0, range)
    print "New game. Range is from 0 to", range
    print "Number of remaining guesses is", remaining_guesses()
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    print
    number_guess = int(guess)
    print "Guess was", number_guess
    global num_guesses
    num_guesses += 1
    print "Number of remaining guesses is", remaining_guesses()
    if number_guess == secret_number:
        print "Correct!"
        new_game()
    elif remaining_guesses() == 0:
        print "You ran out of guesses.  The number was", secret_number
        new_game()
    elif number_guess < secret_number:
        print "Higher!"
    else:
        print "Lower!"
    
# create frame
frame = simplegui.create_frame("Guess The Number", 400, 200)

# register event handlers for control elements and start frame
button100 = frame.add_button('Range is [0,100]', range100)
button1000 = frame.add_button('Range is [0,1000]', range1000)
inp = frame.add_input('Guess Number', input_guess, 50)

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
frame.start()