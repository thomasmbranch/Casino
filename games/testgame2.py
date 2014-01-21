import random

def helper():
    x=random.random()
    if x>.66:
        return True
    return False

def play(user):
    print "Welcome, "+user.getName()
    if helper():
        print "win"
        user.addCredits(20)
    else:
        print "lose"
        user.addCredits(-10)
    return



#put your test code here:
if __name__=="__main__":
    myUser = User('rlba','abcdefg')
    play()
