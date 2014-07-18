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
    
    if user.getCredits()<10:
        print "Insufficient funds!"
        return

    print "Hello,",user.getName()
    if helper():
        print "you win!"
        user.addCredits(10)
    else:
        print "you lose"
        user.addCredits(-10)
    return


## COPY FROM HERE DOWN TO THE BOTTOM OF YOUR FILE ##
if __name__=="__main__":

    # Here is where the test code goes. You should probably leave this
    # unmodified since this is basically what the casino program will be doing.
    # Feel free to ignore this whole block of code, just run your program like
    # you normally would.
    from testUser import User

    myUser = User('unicornmonkeypig123','mypwd','Billy')

    while True:
        play(myUser)
        print "Your balance is %d credits." %myUser.getCredits()
        if raw_input("Play again? (Y/n) ")=='n': break
