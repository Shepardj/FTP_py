'''
functions go in this file
'''


from ftplib import FTP
import getpass
import os

'''
This is how you get a password but this test host doesn't need one
'''
def login(ftpHost):
    '''
    :param : string ftp hostname
    :return: ftp connection object
    '''
    userName = raw_input("User Name: ")
    pw = getpass.getpass("Password(anything will work...): ")

    ftp = FTP(ftpHost,user=userName, passwd=pw)

    del userName
    del pw
    return ftp
