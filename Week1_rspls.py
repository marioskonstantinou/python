import random

def name_to_number(name):
    if (name=="rock"):
        return 0
    elif (name=="Spock"):
        return 1
    elif (name=="paper"):
        return 2
    elif (name=="lizard"):
        return 3
    elif (name=="scissors"):
        return 4
    else:
        return "No matching number found"

def number_to_name(number):
    if (number==0):
        return "rock"
    elif (number==1):
        return "Spock"
    elif (number==2):
        return "paper"
    elif (number==3):
        return "lizard"
    elif (number==4):
        return "scissors"

def rpsls(player_choice): 
    print ""
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    
    if (not isinstance (player_number, int) and (player_number > 4 or player_number < 0)):
        print "Incorrect player selection", player_number
    elif (comp_number > 4 or comp_number < 0):
        print "Incorrect computer selection", comp_number
    else:
        print "Player chooses", player_choice
        print "Computer chooses", number_to_name(comp_number)

        diff_val = (comp_number - player_number) % 5
        if (diff_val == 0):
            print "It's a tie"
        elif (diff_val < 3):
            print "Computer Wins!"
        else:
            print "Player Wins!" 

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
