#Main python file

from ftplib import FTP
from ftp_Library import *
import getpass
import os

api = ftpAPI()
local =LocalFileSystem()

#Welcome to the program prompt
def welcome_for_testing():
    print("\nRunning Steve Fish Truck's FTP Client\n")
    print("You will be automatically logged in to an anonymous FTP client...")

    api.login_for_testing('ftp.edubnetwork.com')
    return

def welcome():
    print("\nRunning Steve Fish Truck's FTP Client\n")
    ftpHost = raw_input("What is ftp host address: ")

    api.login('ftp.edubnetwork.com')
    return


# The help menu
def help():
    space = "   "
    print("The following commands are available: ")

    print("pwd \n" + space + "list current remote directory")
    print("pwd -l \n" + space + "list current local directory")

    print("ls \n" + space + "list files in current remote directory")
    print("ls -l \n" + space + "list files in current local directory")

    print("lsa \n" + space + "list remote files and attributes")
    print("lsa -l \n" + space + "list local files and attributes")

    print("cd \n" + space + "changes to remote root directory")
    print("cd <dirName> \n" + space + "changes to specified remote directory")
    print("cd -l \n" + space + "changes to local root directory")
    print("cd -l <dirName> \n" + space + "changes to specified local directory")

    print("mv <sourceFile> <destinationLocation> \n" + space + "move remote <sourceFile> to remote <destinationLocation>")
    print("mv -l <sourceFile> <destinationLocation> \n" + space + "move local <sourceFile> to local <destinationLocation>")

    print("cp <sourceFile> <destinationFile> \n" + space + "copies a remote <sourceFile> into the <destinationFile>")
    print("cp -l <sourceFile> <destinationFile> \n" + space + "copies a local <sourceFile> into the <destinationFile>")

    print("rm <fileName> \n" + space + "removes <fileName> from remote directory")
    print("rm -l <fileName> \n" + space + "removes <fileName> from local directory")

    print("mkdir <directoryName> \n" + space + "makes a new <directoryName> in current remote directory")
    print("mkdir -l <directoryName> \n" + space + "makes a new <directoryName> in current local directory")

    print("chmod <fileName> <permissionsKey> \n" + space + "changes permissions on remote <fileName> to <permissionsKey>")
    print("chmod -l <fileName> <permissionsKey> \n" + space + "changes permissions on local <fileName> to <permissionsKey>")

    print("get <fileName> \n" + space + "gets <fileName> from current remote directory and stores in current local")
    print("put <fileName> \n" + space + "puts <fileName> from current local directory into current remote directory ")

    print()
    print("help\t: a help menu of available commands and usage")
    print("exit\t: leave the FTP client")
    return

# What happens when the user is done
def exit():
    print("Bye!")
    sys.exit()
    return

# Error help for el usero
def error(message):
    print("<" + message + "> is not a valid command.")
    print("Type help for a list of available commands")
    return()

#~~~~~~~~~~~~ Main Program ~~~~~~~~~~~~~~~#

welcome_for_testing()
print("Type help for a list of available commands")
print

flag = True
isLocal = False
currentPath = api.pwd();   

while flag:
    command = raw_input("[" + currentPath + "] FTP > ")
    cmdParts = command.split()
    cmdLen = len(cmdParts)

    # help, exit, ls, lsa, pwd, cd
    if(cmdLen == 1): 
        cmd = cmdParts[0]    
        if(cmd == "help"):
            help()
        elif(cmd == "exit"):
            exit()
        elif(cmd == "ls"):
            print(api.ls())
        elif(cmd == "lsa"):
            print(api.ls_attributes())
        elif(cmd == "pwd"):
            print(api.pwd())
        elif(cmd == "cd"):
            print(api.cd())
            currentPath = api.pwd()
        else:
            error(command)


    # Checks if it is a local command first
    if(cmdLen > 1):
        # The local flag is always the second 'word' in the command
        if(cmdParts[1] == "-l"):
            print("(Local command heard)")  #debug string
            isLocal = True
        
        # ls -l, lsa -l, pwd -l, cd -l, cd <directory>
        # get <file>, put <file>, mkdir <directory>, rm <file>
        if(cmdLen == 2):
            cmd = cmdParts[0]
            opt = cmdParts[1]
            if(isLocal):
                if(cmd == "pwd"):
                    print(local.pwd())
                elif(cmd == "ls"):
                    print(local.ls())
                elif(cmd == "lsa"):
                    print(local.ls_attributes())
                elif(cmd == "cd"):
                    print(local.cd())
                    currentPath = api.pwd()
                else:
                    error(command)
            else:
                if(cmd == "cd"):
                    print(api.cd(opt))
                    currentPath = api.pwd()
                elif(cmd == "get"):
                    print(api.getFile(opt))
                elif(cmd == "put"):
                    print(api.putFile(opt))
                elif(cmd == "mkdir"):
                    print(api.mkdir(opt))
                elif(cmd == "rm"):
                    print(api.rm(opt))
                else:
                    error(command)

        # cd -l <directory>, rm -l <file>, mkdir -l <directory>
        # mv <source> <dest>, cp <source> <dest>, chmod <file> <permissions>
        elif(cmdLen == 3):
            cmd = cmdParts[0]
            opt1 = cmdParts[1]
            opt2 = cmdParts[2]

            if(isLocal):
                if(cmd == "cd"):
                    print(local.cd(opt2))
                elif(cmd == "rm"):
                    print(local.rm(opt2))
                elif(cmd == "mkdir"):
                    print(local.mkdir(opt2))
                else:
                    error(command)
            else:
                if(cmd == "mv"):
                    print(api.mv(opt1, opt2))
                elif(cmd == "cp"):
                    print(api.cp(opt1, opt2))
                elif(cmd == "chmod"):
                    print(api.chmod(opt1, opt2))
                else:
                    error(command)

        # chmod -l <file> <permissions>, cp -l <source> <dest>, mv -l <source> <dest>
        elif(cmdLen == 4):
            cmd = cmdParts[0]
            opt1 = cmdParts[1]
            opt2 = cmdParts[2]
            opt3 = cmdParts[3]

            if(isLocal):
                if(cmd == "chmod"):
                    print(local.chmod(opt2, opt3))
                elif(cmd == "cp"):
                    print(local.chmod(opt2, opt3))
                elif(cmd == "mv"):
                    print(local.chmod(opt2, opt3))
                else: 
                    error(command)
            else:
                error(command)

        # nonsense command!
        else:
            error(command)

