import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import data
from os.path import expanduser

def send_data():
    msg = MIMEMultipart() 

    msg['From'] = data.sender_email 

    msg['To'] = data.receiver_email

    msg['Subject'] = "Subject of the Mail"

    body = "Body_of_the_mail"

    msg.attach(MIMEText(body, 'plain')) 

    # open the file to be sent 
    filename = 'file.log'

    attachment = open(expanduser(data.path), "rb") 

    p = MIMEBase('application', 'octet-stream') 

    p.set_payload((attachment).read()) 


    encoders.encode_base64(p) 

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 


    msg.attach(p) 

    s = smtplib.SMTP('smtp.gmail.com', 587) 

    s.starttls() 

    s.login(data.sender_email, data.password) 

    text = msg.as_string() 

    s.sendmail(data.sender_email, data.receiver_email, text) 

    s.quit() 
