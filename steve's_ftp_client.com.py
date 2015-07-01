from ftp_Library import *

'''
call functions in the library
'''

api = ftpAPI()



print "user name is Anonymous"
print "no password just hit enter"


api.login('ftp.swfwmd.state.fl.us')

print api.pwd()
print
print api.ls()
print
print api.ls_attributes()


print "\nCurrent directory in local file system"
localFiles = LocalFileSystem()

print localFiles.pwd()