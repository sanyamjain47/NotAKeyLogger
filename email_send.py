import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import data
from os.path import expanduser

# Function to send an email
def send_data():
    # basic setting up the body of the email
    msg = MIMEMultipart() 
    msg['From'] = data.sender_email 
    msg['To'] = data.receiver_email
    msg['Subject'] = "Subject of the Mail"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain')) 

    # open the file to be sent 
    filename = 'file.log'
    attachment = open(expanduser(data.path), "rb") 
    # Some more data that needs to be added with the email when attaching a file
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

    # Attaches the file to the msg
    msg.attach(p) 
    # Starts a google smtp server to send an email
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(data.sender_email, data.password) 
    # Send the data as string
    text = msg.as_string() 

    # Finally send the data
    s.sendmail(data.sender_email, data.receiver_email, text) 
    # Close the server
    s.quit() 
