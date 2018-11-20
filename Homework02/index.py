import simplegui
import random
import math

# initialaze global variables
user_guess = 0
secret_number = 0
num_range = 100
num_guesses = 7


# helper function to start and restart the game
def new_game():
    global secret_number
    global num_guesses
    global num_range
    secret_number = random.randrange(0, num_range)
    num_guesses = math.ceil(math.log(num_range, 2))  # Rounds to nearest integer the log of num_range to base 2
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is", int(num_guesses), "\n"


# helper function to decrement guesses
def decrement_guesses():
    global num_guesses
    num_guesses = num_guesses - 1


# define event handlers for control panel
def range100():
    global num_range
    num_range = 100
    new_game()


def range1000():
    global num_range
    num_range = 1000
    new_game()


# game logic
def input_guess(guess):
    global user_guess
    user_guess = int(guess)
    decrement_guesses()
    print "Guess was", guess
    if int(guess) < secret_number and int(num_guesses) != 0:
        print "Number of remaining guesses is", int(num_guesses)
        print 'Higher!\n'
    elif int(guess) > secret_number and int(num_guesses) != 0:
        print "Number of remaining guesses is", int(num_guesses)
        print 'Lower!\n'
    elif int(guess) != secret_number and int(num_guesses) == 0:
        print "You ran out of guesses.The number was", int(secret_number), "\n"
        new_game()
    elif int(guess) == secret_number:
        print "Number of remaining guesses is", int(num_guesses)
        print "Correct!\n"
        new_game()


# create frame
f = simplegui.create_frame("Game: Guess the number!", 250, 250)

# register event handlers for control elements
f.add_button("Range is [0, 100)", range100, 100)
f.add_button("Range is [0, 1000)", range1000, 100)
f.add_input("Enter your guess", input_guess, 100)

# call new_game and start frame
new_game()
f.start()

