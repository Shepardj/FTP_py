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

def print_menu():
	print("\n----> What can I do for you Steve?? <----\n")
	print("1 = pwd")
	print("2 = ls")
	print("3 = ls_attributes")
	print("4 = Button #4")
	print("99 = Exit! ")
	return

def switch_1():
	print("\npwd")
	print api.pwd()
	return

def switch_2():
	print("\nMORE STUFFF!!!!")
	return

def switch_3():
	print("\nSteve's naughty stuff :)")
	return

def switch_4():
	print("\nButton #4!")
	return

def exit():
	print("\nExiting program.")
	return

#The menu switch, add a -> number : function_name  to it if you'd like a button
def menu(input):
	switch = {
		1 : switch_1,
		2 : switch_2,
		3 : switch_3,
		4 : switch_4,
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


