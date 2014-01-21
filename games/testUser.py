class User(object):

    def __init__(self,uname,passwd,name="default_name"):
        self.username = uname
        self.name = name
        self.credits = 200

    def getUsername(self):
        return self.username

    def getName(self):
        return self.name

    def getCredits(self):
        return self.credits

    def addCredits(self,diff):
        self.credits+=diff
        
