# this project sends the mail without opening gmail app

from email.message import EmailMessage # we are importing emailmessage
import ssl #import ssl for secure connection
import smtplib # importing smtplib for simple mail transfer protocol

email_sender = 'n.somashekar415@gmail.com' # your own gamil
email_password = "" # Replace with your email password/ App pasword
email_receiver = 'rufyuhogno@gufum.com'# recevier email/ Im using temp mail



# in subject and body you can type anything and send 
subject = 'Python projects codes'
body = '''
This is just a practice code for my knowledge.
'''

# em is simple shortfrom of emailmessage
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
