#Import Libraries
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

#Creating server connection
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.ehlo()  

server.login('email', 'password')

#assigning the multiple parts of mail like sender,recepient,subject
message = MIMEMultipart()
message["from"] = "Sender"
message["to"] = "Recepient"
message["Subject"] = "Subject Line"

#Opening the file and reading the message to be sent
with open('message.txt', 'r') as f:
    msg = f.read()

#Attaching the text to mail
message.attach(MIMEText(msg, 'plain'))

#Attaching the image file to mail
filename = 'image.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
message.attach(p)

text = message.as_string()
server.sendmail('sender mail', 'receiver mail', text)