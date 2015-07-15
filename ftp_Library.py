'''
Classess and functions go in this file
Linux style file commands for the server and local file system
'''


from ftplib import FTP
import sys
import getpass
import os


class ftpAPI:



    def __init__(self):
        self.connection = None

    def login(self, ftpHost):
        '''
        :param : string ftp hostname
        :return: ftp connection object
        '''
        # userName = raw_input("User Name: ")
        # pw = getpass.getpass("Password(anything will work...): ")

        self.connection = FTP(ftpHost,user="Anonymous", passwd="")

        # del userName
        # del pw

    def pwd(self):
        return self.connection.pwd()

    def ls(self):
        return self.connection.nlst()

    def ls_attributes(self):
        return self.connection.dir()


    def getFile(self, fileToGet, localDestinationPath):
        print ("Not implemented yet")
    def putFile(self, fileToPut, serverDestinationPath):
        print ("Not implemented yet")
    def cd(self, folderName):
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


class LocalFileSystem:

    def __init__(self):
        self.currentDirectory = os.getcwd()


    def pwd(self):
        return self.currentDirectory

    def ls(self):
        print ("Not implemented yet")
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
