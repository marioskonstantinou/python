import simplegui
import math
import random

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
num_range = 100
remaining_guesses = 0
secret_number = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    # calculate remaining guesses
    global remaining_guesses
    global num_range
    global secret_number

    remaining_guesses = math.ceil(math.log(num_range,2))    
    secret_number = random.randrange(0, num_range)
    print
    print "New game. Range is from 0 to ", num_range
    print "Number of remaining guesses is", remaining_guesses
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    # remove this when you add your code   
    global num_range
    num_range=100
    new_game()    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range=1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    try:
        # try to convert guess into an integer. 
        # throws an exception if guess is not a number
        val = int(guess)    
        print
        print "Guess was", guess
        global remaining_guesses
        global secret_number

        if (int (secret_number) == int (guess)):
            print "Correct!"
            new_game()
        else:
            if (int (guess) > int(secret_number)):
                print "Lower!"
            else:
                print "Higher!"
                
            remaining_guesses = remaining_guesses - 1
            if remaining_guesses == 0:
                print "You ran out of guesses. The number was", secret_number
                new_game()
            else:
                print "Number of remaining guesses is", remaining_guesses

    except ValueError:
        print("Please enter a digit")    

# create frame
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Guess The Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("[0,100) range", range100, 100)
frame.add_button("[0,1000) range", range1000, 100)
frame.add_input("Your guess",input_guess, 200)

# Start the frame animation
frame.start()

# call new_game 
new_game()
