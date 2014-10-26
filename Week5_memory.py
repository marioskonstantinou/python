import simplegui
import random
import math

DIFFERENCE = 50
num_list = []
exposed = []
first_card = 0
last_card = 0
turns = 0

# helper function to initialize globals
def new_game():
    '''Starts new game by creating new number and exposed lists'''
    global num_list, exposed, state, first_card, last_card, turns
    turns = 0
    first_card = 0
    last_card = 0
    state = 0
    num_list = []
    
    # Set turns label to 0
    label.set_text('Turns = '+str(turns))
    
    for x in range(0, 2):
        for i in range(0, 8): 
            num_list.append(i)
    random.shuffle(num_list)
    exposed = [False for i in range(16)]
    
# define event handlers
def mouseclick(pos):
    '''Reveal clicked card if not exposed and increase no of turns'''
    global exposed, state, first_card, last_card, turns

    # Find index of clicked card
    card_clicked = int(math.ceil(pos[0]/50))
    
    # Proceed only if card is not exposed
    if not exposed[card_clicked]:
        exposed[card_clicked] = True
        
        if state == 0:
            first_card = card_clicked
            state = 1
        elif state == 1:
            # Increase number of turns
            turns+=1
            last_card = card_clicked
            state = 2
        else:
            # if the two cards do not match hide them
            if num_list[first_card] != num_list[last_card]:
                exposed[first_card] = False
                exposed[last_card] = False
            first_card = card_clicked
            state = 1
        # Set number of turns
        label.set_text('Turns = '+str(turns))            
   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    '''Draw cards and if not exposed hide them'''
    global exposed, num_list
    cur_pos = 15
    
    for i in range(len(num_list)):
        canvas.draw_text(str(num_list[i]), [cur_pos, 60], 30, "White")
        cur_pos+=DIFFERENCE

    position = -DIFFERENCE

    for z in exposed:
        position += DIFFERENCE
        if not z:
            canvas.draw_polygon([(position, 0), 
                                 (position + DIFFERENCE, 0), 
                                 (position + DIFFERENCE, 100), 
                                 (position , 100)], 3, "Gray", "Green")

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = "+str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()