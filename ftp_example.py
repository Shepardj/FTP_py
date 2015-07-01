from ftplib import FTP
import getpass
import os

'''
This is how you get a password but this test host doesn't need one
'''
# userName = raw_input("User Name: ")
# pw = getpass.getpass("Password(anything will work...): ")

#from https://www.swfwmd.state.fl.us/data/ftp/
host = 'ftp.swfwmd.state.fl.us'
userName = 'Anonymous'
pw = ''


'''
Create the connection
'''

ftp = FTP(host,user=userName, passwd=pw)

#delete users password!!!!!!!!!!!!
del userName
del pw

#pretty print a dir on the server
print "contents of current directory"
print ftp.dir()

print "contents of pub directory"
print ftp.dir('pub')



#get contents of a directory in a python list
listOfServerDirectory = ftp.nlst()
print listOfServerDirectory
print
#change directory
print 'change directory to pub'
print ftp.cwd('pub')

print
print "current dir is: "
print ftp.pwd()


for afile in os.listdir("./"):
    print afile
