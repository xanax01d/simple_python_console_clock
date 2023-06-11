from datetime import datetime
import sys as s
from time import sleep
from art import * 
from os import system
from ctypes import windll
import subprocess as sp
import os,locale,yaml,pyowm,asyncio,psutil,win32gui,win32con


class info: pass #dynamic class
def exitt():
	clear_console()
	print('Exit...')
	exit()

system("title " + 'Clocks')
with open("settings.yaml", "r") as f:
    settings = yaml.load(f, Loader=yaml.FullLoader) # open config

locale.setlocale(
	category = locale.LC_ALL,
	locale = settings['language']) #set language


def change_size(): 
	if settings["clock_type"] == 1:
		return(os.system('mode 42,10'))
	else:
		if settings["show_day_and_date"] == 3:
			return(os.system('mode 42,8'))
		else:
			return(os.system('mode 32,8'))
def clear_console(): #clear console\terminal
	if s.platform == 'linux' or s.platform == 'linux2':
		return(os.system('clear'))
	elif s.platform == 'win32':
		return(os.system('cls'))
	elif s.platform == 'darwin':
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
	if settings["show_active_window"] == 1:
		print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
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
	# Qold_style = win32con.GetWindowStyle()
	#$win32con.SetWindowStyle(old_style | wx.STAY_ON_TOP)
	main()