import smtplib
import csv
import time
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#server and file context variables
csv_filename = "dummy.csv"
text_body_filename = "textbody.txt"
html_body_filename = "htmlbody.txt"
sender = "Do Not Reply <donotreply@domain.ca>"
subject = "Your Subject Line"
smtp_hostname = "smtp.domain.ca"
smtp_port = 2525
smpt_username = "USERNAME"
smtp_password = "PASSWORD"

#define a deliver_message function to create and deliver a well formed multipart MIMEText object 
def deliver_message(server, sender, receiver, subject, text, html):
    #setup message and header
    message = MIMEMultipart('alternative')  
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    message['Message-id'] = email.utils.make_msgid()
    message['Date'] = email.utils.formatdate()
    #create the multipart MIMEText
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    #attach to the message
    message.attach(part1)
    message.attach(part2)
    #send the message
    server.sendmail(sender, receiver, message.as_string())

#setup csv reader
csvfile = open(csv_filename, 'r')
datareader = csv.reader(csvfile)

#open server connection
#server.set_debuglevel(2)
server = smtplib.SMTP(smtp_hostname, smtp_port)
server.login(smpt_username, smtp_password)

#iterate through the csv and send a personalised message
for row in datareader:
    
    #setup variables for name and address
    first_name = row[0]
    last_name = row[1]
    email_address = row[3]
    receiver = first_name +" "+ last_name +" <"+ email_address +">"
    
    #import the text and html bodies and format them with the first name
    text = open(text_body_filename, 'r').read().format(first_name)
    html = open(html_body_filename, 'r').read().format(first_name)

    #pass values to deliver_message function
    deliver_message(server, sender, receiver, subject, text, html)
    
    #wait a bit
    time.sleep(3)

#after the loop quit the server connection
server.quit()