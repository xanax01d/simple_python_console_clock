from datetime import datetime
import os
from sys import platform,exit
from time import sleep
from art import *
import locale
import yaml

with open("settings.yaml", "r") as f:
    settings = yaml.load(f, Loader=yaml.FullLoader) # open config
locale.setlocale(
	category = locale.LC_ALL,
	locale = settings['language']) #set language

class info: pass #dynamic class
def exitt():
	clear_console()
	print('Exit...')
	exit()

def change_size(): 
	if settings["clock_type"] == 1:
		return(os.system('mode 38,7'))
	else:
		return(os.system('mode 25,7'))
def clear_console(): #clear console\terminal
	if platform == 'linux' or platform == 'linux2':
		return(os.system('clear'))
	elif platform == 'win32':
		return(os.system('cls'))
	elif platform == 'darwin':
		return(os.system('clear'))

def get_time(info): #getting time,date,day
	info.day = datetime.now().strftime("%A")
	if settings["clock_type"] == 1:
		info.t = datetime.now().strftime("%H:%M:%S")
	else:
		info.t = datetime.now().strftime("%H:%M")
	info.full_date = datetime.now().strftime("%d.%m.%Y")
	return info()

def printtime(info): #printing time,day and date
	tprint(info.t,font = settings["font"]) 
	if settings["show_day_and_date"] == 3:
		print(info.day,'\t\t',info.full_date)
	elif settings["show_day_and_date"] == 2:
		print(info.day)
	elif settings["show_day_and_date"] == 1:
		print(info.full_date)
	sleep(0.5)
	clear_console()

def main():
	change_size()
	while True:
		try:
			printtime(get_time(info))
		except KeyboardInterrupt:
			exitt()

if __name__ == '__main__':
	main()