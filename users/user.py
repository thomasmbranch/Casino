"""
User Class--
Ryerson Lehman-Borer
January 2014

User object class for the casino game. Each user object stores all a user's data
while the user is "logged on" through the casino. Whenever the object is
modified, the changes are written to a file on disk that stores all data about
the user long term.

each User has data members:
    username
    passhash (md5 hash of password)
    name     (first name or nickname)
    credits
    
User class methods:
    updateUserFile -- write user data to disk
    unpackUserFile -- load user data from disk
    getUsername -- return user's username
    getName -- return user's nickname
    setName -- change user's nickname
    getCredits -- return user's balance
    addCredits -- add credits to a user's balance (positively or negatively)
    changePassword -- update password and re-encrypt data on disk

"""
import hashlib

class User(object):

    def __init__(self, uname, passwd, name=""):

        #compute hash of passwd
        m = hashlib.md5(passwd)
        self.passhash = m.digest()

        if name=="":    #user already exists; read user data from file
            self.unpackUserFile(uname)
        else:           #create user
            try:
                filename = "users/" + uname + ".cud" 
                open(filename)
                raise RuntimeError("username already exists")
            except IOError:
                pass
            self.username = uname
            self.name = name
            self.credits = 200
            #self.achievements = [] #list of achievement objects
            self.updateUserFile()
    
    def updateUserFile(self):
        """Write all of user's data to a file in the users/ directory
        If file doesn't exist yet, it is created
        user data files are named with file extension .cud (Casino User Data)
        """
        #build up data to be stored in file
        fileData = ""
        fileData += self.username + '\n'
        fileData += self.name + '\n'
        fileData += str(self.credits) + '\n'
        #achievements can be added in string form here

        fileData = xorCipher(fileData,self.passhash)
        
        #write data to file
        #note: made up filetype 'Casino User File'
        filename = "users/" + self.username + ".cud" 
        inf = open(filename, 'w')
        inf.write(fileData)
        inf.close()
        return


    def unpackUserFile(self,uname):
        """Read in user's data file and initialize object
        Throw an exception if password is incorrect or user data file not found
        input uname: username
        return: None
        """
        #check to see that file exists
        filename = "users/" + uname + ".cud" 
        try:
            #make sure user data file exists
            inf = open(filename,'r')
            fileData = inf.read()
            inf.close()

            fileData = xorCipher(fileData,self.passhash)
            data = fileData.split('\n')
        
            if uname!=data[0]:
                raise RuntimeError("invalid username or password")
            self.username = data[0]
            self.name = data[1]
            self.credits = int(data[2])
            #self.achievements = []
            
            return

        except IOError: #check constructor usage
            raise RuntimeError("invalid username")

    

    """
    Getters/Setters
    Mostly self explanatory. Setters call updateUserFile()
    so that data files are always up to date
    """

    def getUsername(self):
        return self.username

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        self.updateUserFile()

    def getCredits(self):
        return self.credits

    def addCredits(self, difference):
        self.credits += difference
        self.updateUserFile()

    def changePassword(oldpwd, newpwd):
        """changes password (as long as old password is a match)
        re-encrypts all data with new password
        returns True if successful, False if passwords don't match
        """
        m = hashlib.md5(oldpwd)
        if self.passhash != m.digest():
            return False
        else:
            m.update(newpwd)
            self.passhash = m.digest()
            self.updateUserFile()
            return True
        
        
        
def xorCipher(string,key):
    """Encrypts/Decrypts strings using xor cipher
    NOT part of the User class
    input string: string to be shifted
    input key: key to shift with
    return: None
    """
    charList = [ord(ch) for ch in string]
    for i in range(len(charList)):
        charList[i] = chr(charList[i] ^ ord(key[i%16]))
    string = ''.join(charList)
    return string



    

if __name__=="__main__":

    myUser = User('rlba','abcdefg')
    play(myUser)
