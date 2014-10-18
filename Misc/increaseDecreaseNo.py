import simplegui

total = 5
pressed = 0

def keydown(key):
    global total, pressed
    total*=2
    pressed+=1
    print total
    print 'Pressed: ', pressed
    
def keyup(key):
    global total
    total-=3
    print total

def draw(canvas):
    global total
    print total
    
# create frame 
frame = simplegui.create_frame("Increase/Decrease No", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)