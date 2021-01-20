#This Code is Written by Sachin Shrivastv
#coding = utf-8

import os, time, sys

os.system('clear')

def printing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)
logo=''' .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. |
| |    ______    | | |     ____     | | |     __       | |
| |   / ____ `.  | | |   .'    '.   | | |    /  |      | |
| |   `'  __) |  | | |  |  .--.  |  | | |    `| |      | |
| |   _  |__ '.  | | |  | |    | |  | | |     | |      | |
| |  | \____) |  | | |  |  `--'  |  | | |    _| |_     | |
| |   \______.'  | | |   '.____.'   | | |   |_____|    | |
| |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '''

 
logo2='''  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
 
def login():
	print(logo)
	print(logo2)
	print('                     Owner:-    Badhshah')
	print('                     Author:-   Sachin Shrivastv')
	print('                     Youtube:-  Badhshah Hacker')
	print('                     Whatsapp:- +977-9845844301')
	print(logo2)
	username = raw_input('  Username:- ')
	if username =='':
		print(' [!] Invalid Username')
		time.sleep(1)
		os.system('clear')
		login()
	elif username =='Hacker':
		password = raw_input('  Password:- ')
		if password =='':
			print(' [!] Invalid Password')
			time.sleep(1)
			os.system('clear')
			login()
		elif password =='Badhshah':
			printing('  Logged Successful ')
			os.system('python2 base.py')
		else:
			print(' [!] Invalid Password')
			time.sleep(1)
			os.system('clear')
			login()
	else:
		print(' [!] Invalid Username')
		time.sleep(1)
		os.system('clear')
		login()
		
login()