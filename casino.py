#!/usr/bin/python
from users.user import User
from getpass import getpass

def main():

    #import each module listed in the gamelist.txt
    inf = open("games/gamelist.txt")
    gamelist = [l.split('|') for l in inf]
    inf.close()
    module = [__import__("games."+mod[0], fromlist=['blah']) for mod in gamelist]


    user = getUser()

    while True:
        print """\n\nOptions:
        1) Play a game
        2) Print User Data
        3) Log Out (quit)
        """
        choice = input("choice: ")
        while (choice<=0 or choice>3):
            print "invalid choice, please try again"
            choice = input("choice: ")

        if choice==1: playGame(user, gamelist, module)
        if choice==2: printUserData(user)
        if choice==3: break


"""get username and password from user, load user data
return user object"""
def getUser():

    print "\nWelcome to our Casino! Please enter your credentials below.\n"

    #determine whether to create new account or load old one
    create = "blah"
    while create not in ['','create']:
        create = raw_input("Type 'create' to make a new account"
                " or hit Enter to proceed to log in\n").lower()
    if create=='create':    #new user; get name
        name = raw_input("name: ")

    #get account credentials
    uname = raw_input("username: ")
    password = getpass("password (nothing will appear on screen) : ")

    if create=='create':    #create new account
        password2 = getpass("confirm password: ")

        while password != password2:
            print "\nPasswords did not match, please re enter."
            password = getpass("password: ")
            password2 = getpass("confirm password: ")

        while True:
            try:
                myUser = User(uname,password,name)
                break
            except RuntimeError:
                print "\nusername '%s' already taken, try a different one." %uname
                uname = raw_input("new username: ")
        print "Account creation successful."

    else:   #load account data from disk
        while True:
            try:
                myUser = User(uname,password)
                break
            except RuntimeError:
                print "Invalid username or password. Please try again."
                uname = raw_input("username: ")
                password = getpass("password: ")
        print "Welcome back,", myUser.getName()

    return myUser

"""print User's data, such as username, credits"""
def printUserData(user):
    #TODO expand to be able to modify name, password
    print "\nUser Data for",user.getUsername()
    print "name:",user.getName()
    print "credits:",user.getCredits()
    print ""
    return

"""select a game, play as many times as user would like to and is able to"""
def playGame(user,gamelist,module):

    print "which game would you like to play?"
    for i in range(len(gamelist)):
        print str(i+1) + ") " + gamelist[i][1]

    choice = input("choice: ")
    while (choice<=0 or choice>len(gamelist)):
        print "invalid choice, please try again"
        choice = input("choice: ")

    while True:
        module[choice-1].play(user)

        print "Your balance is now %d credits." %user.getCredits()
        again = raw_input("play again? (Y/n)")
        if again=='n':
            break

    return


if __name__=="__main__":
    main()
