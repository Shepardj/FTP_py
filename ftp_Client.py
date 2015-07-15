#Main python file

from ftplib import FTP
from ftp_Library import *
import getpass
import os

api = ftpAPI()

#Variables:
flag = 1

#Welcome to the program prompt
def welcome(): 
	print("\nWelcome to the program Steve Fish Truck\n")  #someone make this better :)
	print "user name is Anonymous"
	print "no password just hit enter"

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
		99 : exit
	}

	func = switch.get(input, lambda: "Bad number") #default case = error of -1

	return func()


#~~~~~~~~~~~~ Main Program ~~~~~~~~~~~~~~~#

welcome()
while flag == True:
	print_menu()
	response = input('\nEnter menu selection: ')
	menu(response)
	if response == 99:
		break


