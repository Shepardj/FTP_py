#Main python file

from ftplib import FTP
from ftp_Library import *
import getpass
import os

api = ftpAPI()
local =LocalFileSystem()

#Variables:
flag = 1

#Welcome to the program prompt
def welcome_for_testing():
    print("\nWelcome to the program Steve Fish Truck\n")  #someone make this better :)
    print "user name is Anonymous"
    print "no password just hit enter"

    api.login_for_testing('ftp.swfwmd.state.fl.us')
    return

def welcome():
    print("\nWelcome to the program Steve Fish Truck\n")  #someone make this better :)
    ftpHost = raw_input("What is ftp host address: ")
    api.login('ftp.swfwmd.state.fl.us')
    return


# This is the worst way we could do this....
def print_menu():
    print("\n----> What can I do for you Steve?? <----\n")
    print("1 = pwd")
    print("2 = ls")
    print("3 = ls_attributes")
    print("4 = getFile")
    print("5 = putFile")
    print("6 = cd")
    print("7 = cp")
    print("8 = mv")
    print("9 = rm")
    print("10 = mkdir")
    print("11 = chmod")
    print("12 = local_pwd")
    print("13 = local_ls")
    print("14 = local_ls_attributes")
    print("15 = local_cd")
    print("16 = local_cp")
    print("17 = local_mv")
    print("18 = local_rm")
    print("19 = local_mkdir")
    print("20 = local_chmod")
    print("99 = Exit! ")
    return

def pwd():
    print("\npwd")
    print api.pwd()
    return

def ls():
    print("\nls")
    print api.ls()
    return

def ls_attributes():
    print("\nls_attributes")
    print api.ls_attributes()
    return

def getFile():
    print("\ngetFile")
    print api.getFile()
    return

def putFile():
    print("\nputFile")
    print api.putFile()
    return

def cd():
    print("\ncd")
    print api.cd()
    return

def cp():
    print("\ncp")
    print api.cp()
    return

def mv():
    print("\nmv")
    print api.mv()
    return

def rm():
    print("\nrm")
    print api.rm()
    return

def mkdir():
    print("\nmkdir")
    print api.mkdir()
    return

def chmod():
    print("\nchmod")
    print api.chmod()
    return

def local_pwd():
    print("\nlocal_pwd")
    print local.pwd()
    return

def local_ls():
    print("\nlocal_ls")
    print local.ls()
    return

def local_ls_attributes():
    print("\nlocal_ls_attributes")
    print local.ls_attributes()
    return

def local_cd():
    print("\nlocal_cd")
    print local.cd()
    return

def local_cp():
    print("\nlocal_cp")
    print local.cp()
    return

def local_mv():
    print("\nlocal_mv")
    print local.mv()
    return

def local_rm():
    print("\nlocal_rm")
    print local.rm()
    return

def local_mkdir():
    print("\nlocal_mkdir")
    print local.mkdir()
    return

def local_chmod():
    print("\nlocal_chmod")
    print local.chmod()
    return


def exit():
    print("\nExiting program.")
    return

#The menu switch, add a -> number : function_name  to it if you'd like a button
def menu(input):
    switch = {
        1 : pwd,
        2 : ls,
        3 : ls_attributes,
        4 : getFile,
        5 : putFile,
        6 : cd,
        7 : cp,
        8 : mv,
        9 : rm,
        10: mkdir,
        11: chmod,
        12: local_pwd,
        13: local_ls,
        14: local_ls_attributes,
        15: local_cd,
        16: local_cp,
        17: local_mv,
        18: local_rm,
        19: local_mkdir,
        20: local_chmod,
        99: exit
    }

    func = switch.get(input, lambda: "Bad number") #default case = error of -1

    return func()


#~~~~~~~~~~~~ Main Program ~~~~~~~~~~~~~~~#

welcome_for_testing()
while flag == True:
    print_menu()
    response = input('\nEnter menu selection: ')
    menu(response)
    if response == 99:
        break


