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



