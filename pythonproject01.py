#Send an Email: Use Python to successfully send an email.  

import smtplib
from email.message import EmailMessage

#Creating an email
msg = EmailMessage()
msg['Subject'] = 'Hello from Python!'
msg['From'] = 'whoisitfrom@gmail.com' #Enter the sender Email address
msg['To'] = 'to_mee@gmail.com' #Enter the reciever Email address
msg.set_content('Hey! This email was sent using Python.')

#Sending the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #Enter the sender Email address and the App Password
    smtp.login('whoisitfrom@gmail.com', '>App Password<') 
    smtp.send_message(msg)

print("✅ Email sent!")