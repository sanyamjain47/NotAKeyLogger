from ftplib import FTP
from data import ftp_address,ftp_username,ftp_password, path
import os

filename = os.path.expanduser(path)
ftp = FTP(ftp_address)
ftp.login(ftp_username,ftp_password)
with open(filename, "rb") as file:
    ftp.storbinary("STOR test.log", file)
ftp.quit()