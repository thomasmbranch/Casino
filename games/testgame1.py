import random

def helper():
    #this is a function that is called by play()
    #you can have as many of these as you want
    x=random.random()
    if x>.5:
        return True
    return False

def play(user):
    #this function is called at the beginning of each game.
    if helper():
        print "win"
        user.addCredits(10)
    else:
        print "lose"
        user.addCredits(-10)
    return



if __name__=="__main__":
    #put your test code here:

    myUser = User('rlba','abcdefg')
    play()
