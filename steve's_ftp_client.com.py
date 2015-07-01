from ftp_Library import *

'''
call functions in the library
'''

print "user name is Anonymous"
print "no password just hit enter"


ftp = login('ftp.swfwmd.state.fl.us')

print ftp.dir()

