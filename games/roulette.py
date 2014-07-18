import random

def play(credits, uname):
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
    while OperationFinished > 1:
        choosenum = input('What number would you like to place your bet on? (1-36)');
        if choosenum < 37 and choosenum > 0:
            OperationFinished = 1;
        else:
            print ('sorry, that is not a valid number.');
    return choosenum

def getBetAmnt():
    OperationFinished = 0;
    while OperationFinished > 1:
        choosebet = input('How many credits will you bet?');
        if choosebet < credits+1 and choosebet > 0:
            OperationFinished = 1;
        else:
            print ('sorry, that is not a valid bet.');

def spin():
    x=random.random()
    if x>.0278:
        return True
    return False

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

