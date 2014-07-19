""" NOTES TO NOAH:
  Noah, this is a good first draft. I think you will find it won't work properly
  yet, and there are a few reasons. That said, you're definitely on the right
  track, and with a bit of careful debugging (a very important skill), you
  should be able to fix it up.
  I've added comments on/near a few lines that I think may be problematic for
  you in order to jump start the debugging process, but I tried not to just tell
  you how to fix it--you'll have to figure out what the problem is. There are
  also a couple of things that may or may not be problems that I didn't bother
  to flag. Make sure you test carefully to ensure everything is working the way
  you want it to!
  I also noticed that you had no comments. Fix that.

  Keep up the good work!
"""
import random

def play(user): #play must take a user object as its only argument
    #here is how you can get these data members from the object
    credits=user.getCredits()
    uname=user.getUsername() #alternatively use getName()

    pick=getUserNum()
    bet=getBetAmnt()
    if spin():
        print('You Win!');
        return bet*30
    else:
        print('You Lose');
        return bet*-1

def getUserNum():
    OperationFinished = 0;
    while OperationFinished > 1:  #this while loop will never run. Why?
        choosenum = input('What number would you like to place your bet on? (1-36)');
        if choosenum < 37 and choosenum > 0:
            OperationFinished = 1;
        else:
            print ('sorry, that is not a valid number.');

    #since the while loop never happens, choosenum will never have been defined
    return choosenum

def getBetAmnt():
    OperationFinished = 0;
    while OperationFinished > 1:  #same problem with this while loop
        choosebet = input('How many credits will you bet?');
        if choosebet < credits+1 and choosebet > 0: #there's a <= comparator
            OperationFinished = 1;
        else:
            print ('sorry, that is not a valid bet.');
    #missing something?

def spin():
    x=random.random()
    if x>.0278:
        return True
    return False


### Everything from here on down is test code; you probably shouldn't modify it
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

