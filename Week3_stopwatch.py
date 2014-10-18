import simplegui

# define global variables
currentms=0
success=0
currenttry=0
currentattempts="0/0"
stops=0
isStarted=False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    '''Calculate A, BC and D and return formatted string'''    
    # D
    ms = (t % 10)
    # BC
    sec = ((t - ms) // 10) % 60
    # A
    mins = str(((t - ms) // 600))

    # Subtract 60 when seconds reach 60     
    if (sec >= 60): 
        sec -= 60

    # Add leading 0 if seconds are less than 10
    secondsValue = str(sec)
    if (sec < 10):
        secondsValue = "0"+secondsValue
    
    return mins + ":" + secondsValue + "." + str(ms)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    '''Start timer and increase ms by 1'''
    timer.start()
    global currentms, isStarted
    currentms+=1
    isStarted = True
    
def stop():
    global isStarted
    if isStarted:
        '''Stop timer and calculate success/currenttry'''
        timer.stop()
        global currentms
        global currenttry
        global currentattempts
        global success
        currenttry+=1
        if (currentms%10==0):
            success+=1
        currentattempts = str(success)+ '/'+str(currenttry)
        isStarted=False

def reset():
    '''Stop timer and reset all global variables'''
    timer.stop()
    global currentms
    global currenttry
    global currentattempts
    global success    
    currentms=0   
    success=0
    currenttry=0
    currentattempts="0/0"

# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, start)

# define draw handler
def draw(canvas):
    canvas.draw_text(format(currentms), [50,100], 30, "White")
    canvas.draw_text(currentattempts, [140,30], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
frame.set_draw_handler(draw)

# start frame
frame.start()