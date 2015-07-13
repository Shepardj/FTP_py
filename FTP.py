#Main python file


#~~~~~~~~~~~~ Pre Program Stuff ~~~~~~~~~~~~~~~#

from ftplib import FTP
from ftp_Library import *
import getpass
import os

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


#~~~~~~~~~~~~~~~~ Variables/Definitions ~~~~~~~~~~~~~~~~~~~~~~~#

#Variables:
flag = 1

#Welcome to the program prompt
def welcome(): 
	print("\nWelcome to the program Steve Fish Truck\n")  #someone make this better :)
	return

def print_menu():
	print("\n----> What can I do for you Steve?? <----\n")
	print("1 = Some Stuff")
	print("2 = More Stuff")
	print("3 = Steve's Stuff!")
	print("4 = Button #4")
	print("99 = Exit! ")
	return

def switch_1():
	print("\nI DID SOME STUFF!!!!")
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

def menu(input):
	switch = {
		1 : switch_1,
		2 : switch_2,
		3 : switch_3,
		4 : switch_4,
		99 : exit
	}

	func = switch.get(input, lambda: -1) #default case = error of -1

	return func()


#~~~~~~~~~~~~ Main Program ~~~~~~~~~~~~~~~#

welcome()
while flag == True:
	print_menu()
	response = input('\nEnter menu selection: ')
	menu(response)
	if response == 99:
		break


