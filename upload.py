from ftplib import FTP
from data import ftp_address,ftp_username,ftp_password
import os

def upload_file(file_name):
    filename = os.path.expanduser(file_name)
    ftp = FTP(ftp_address)
    ftp.login(ftp_username,ftp_password)
    with open(filename, "rb") as file:
        ftp.storbinary(f"STOR {filename.split('/')[-1]}", file)
    ftp.quit()