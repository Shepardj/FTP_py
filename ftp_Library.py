'''
Classess and functions go in this file
Linux style file commands for the server and local file system
'''


from ftplib import FTP
import ftplib
import sys
import getpass
import os
import shutil


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

        #auto login for testing ease
        try:
            self.connection = FTP(ftpHost,user="stevefisheries", passwd="1mactruck2") #for connecting to new server
        except:
            print("Login Failed. Check User Name and Pass Word.")
            exit()
        # del userName
        # del pw

    def pwd(self):
        return self.connection.pwd()

    def ls(self):
        formattedDirs = "\n".join(self.connection.nlst())
        return formattedDirs
        #return self.connection.nlst()

    def ls_attributes(self):
        return self.connection.dir()

    def getFile(self, fileToGet, localDestinationPath=os.getcwd()):
        if(fileToGet in self.connection.nlst()):
            command = "RETR " + fileToGet
            return self.connection.retrlines(command,  open(fileToGet, 'wb').write)
        else:
            raise FileNotFoundException("Cannot find <" + fileToGet + ">")

    def putFile(self, fileToPut):
        self.currentDirectory = os.getcwd()
        dirs = os.listdir(self.currentDirectory)
        if(fileToPut in dirs):
            command = "STOR " + fileToPut
            return self.connection.storlines(command, open(fileToPut, 'r'))
        else:
            raise FileNotFoundException("Cannot find <" + fileToPut + ">")

    def cd(self, folderName='/'):
        if(folderName == "/"):
            return self.connection.cwd('/')
        if(folderName in self.connection.nlst()):
            try:
                return self.connection.cwd(folderName)
            except ftplib.error_perm as e:
                return "Unexpected error: " + str(e)
        else:
            return "Cannot cd into <" + folderName + ">"

    def cp(self, source, dest, tempLocalStorage=os.getcwd()):
        if(source in self.connection.nlst()):
            command = "RETR " + source
            response = self.connection.retrlines(command, open(source, 'wb').write)
            command = "STOR " + dest
            return self.connection.storlines(command, open(source, 'r'), open(dest, 'wb').write)
        else:
            raise FileNotFoundException("Cannot find <" + source + ">")

    def mv(self, source, dest):
        if(source in self.connection.nlst()):
            return self.connection.rename(source, dest)
        else:
            raise FileNotFoundException("Cannot find <" + source + ">")

    def rm(self, fileName):
        if(fileName in self.connection.nlst()):
            try:
                self.connection.delete(fileName)
                print("removed file: " + fileName)
                return
            except ftplib.error_perm, resp:
                print("Cannot remove! " + fileName + " is not a file!")
                return
        else:
            print("failed to remove file! " + fileName + " does not exist!")
            return

    def mkdir(self, directoryName):
        if(directoryName in self.connection.nlst()):
          print("failed to create directory! " + directoryName + " already exists!")
          return
        else:
          self.connection.mkd(directoryName);
          print("created directory: " + directoryName)

    def rmdir(self, directoryName):
      if(directoryName in self.connection.nlst()):
          try:
            self.connection.rmd(directoryName)
            print("removed directory: " + directoryName)  
            return
          except ftplib.error_perm, resp:  
            print("Cannot remove! " + directoryName + " is not a directory!")
            return
      else:  
        print("failed to remove directory! " + directoryName + " does not exist!")
        return

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
        print ("Not implemented yet, not sure if python OS has this ability")
    def cd(self, fileName):
        print ("Not implemented yet")
    def cp(self, fileName):
        print ("Not implemented yet")

    def mv(self, source, dest):
        if(os.path.isfile(source)):
            os.rename(source, dest)
            string = "File " + source + " renamed -> " + dest
            return string
        else:
            raise FileNotFoundException("Cannot find <" + source + ">")

    def rm(self, fileName):
        if(os.path.isfile(fileName)):
            os.remove(fileName)
            string = "File " + fileName + "removed"
            return string
        elif(os.path.isdir(fileName)):
            shutil.rmtree(fileName)
            string = "File " + fileName + " removed"
            return string
        else:
            raise FileNotFoundException("Cannot find <" + fileName + ">")

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
