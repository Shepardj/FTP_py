'''
Classess and functions go in this file
Linux style file commands for the server and local file system
'''


from ftplib import FTP
import sys
import getpass
import os


class ftpAPI:
    '''
    Useful Documentation: https://docs.python.org/2/library/ftplib.html
    '''



    def __init__(self):
        self.connection = None

    def login(self, ftpHost):
        '''
        :param : string ftp hostname
        :return: ftp connection object
        '''
        userName = raw_input("User Name: ")
        pw = getpass.getpass("Password: ")
        try:
            self.connection = FTP(ftpHost,user=userName, passwd=pw)
            del userName
            del pw
        except:
            del userName
            del pw
            print("Login Failed. Check Host, User Name, and Password.")
            exit()



    def login_for_testing(self, ftpHost):
        '''
        :param : string ftp hostname
        :return: ftp connection object
        '''
        # userName = raw_input("User Name: ")
        # pw = getpass.getpass("Password(anything will work...): ")
        try:
            self.connection = FTP(ftpHost,user="Anonymous", passwd="")
        except:
            print("Login Failed. Check User Name and Pass Word.")
            exit()
        # del userName
        # del pw

    def pwd(self):
        return self.connection.pwd()

    def ls(self):
        return self.connection.nlst()

    def ls_attributes(self):
        return self.connection.dir()

    def getFile(self, fileToGet, localDestinationPath=os.getcwd()):
        if(fileToGet in self.connection.nlst()):
            command = "RETR " + fileToGet
            return self.connection.retrlines(command,  open(fileToGet, 'wb').write)
        else:
            raise FileNotFoundException("Cannot find <" + fileToGet + ">")

    def putFile(self, fileToPut, serverDestinationPath):
        print ("Not implemented yet")

    def cd(self, folderName='/'):
        if(folderName == "/"):
            return self.connection.cwd('/')
        if(folderName in self.connection.nlst()): 
            try:
                return self.connection.cwd(folderName)
            except:
                print "Unexpected error:", sys.exc_info()[0]   # I'm not sure how to raise this permissions expection
        else:  
            raise NotADirectoryException("Cannot cd into <" + folderName + ">")

    def cp(self, fileName):
        print ("Not implemented yet")
    def mv(self, fileName):
        print ("Not implemented yet")
    def rm(self, fileName):
        print ("Not implemented yet")
    def mkdir(self, fileName):
        print ("Not implemented yet")
    def chmod(self, fileName):
        print ("Not implemented yet")


class LocalFileSystem:
    '''
    Useful Documentation: https://docs.python.org/2/library/ftplib.html
    '''

    def __init__(self):
        self.currentDirectory = os.getcwd()


    def pwd(self):
        return self.currentDirectory

    def ls(self):
        self.currentDirectory = os.getcwd()
        dirs = os.listdir(self.currentDirectory)
        formattedDirs = "\n".join(dirs)
        return formattedDirs
    
    def ls_attributes(self):
        print ("Not implemented yet")
    def cd(self, fileName):
        print ("Not implemented yet")
    def cp(self, fileName):
        print ("Not implemented yet")
    def mv(self, fileName):
        print ("Not implemented yet")
    def rm(self, fileName):
        print ("Not implemented yet")
    def mkdir(self, fileName):
        print ("Not implemented yet")
    def chmod(self, fileName):
        print ("Not implemented yet")


class FileNotFoundException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NotADirectoryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
