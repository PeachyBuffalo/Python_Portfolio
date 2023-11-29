from email.message import EmailMessage
from app_pass import password, email_sender
import ssl
import smtplib


#Requires 'App Password' from Google
email_sender = ''
email_password = password

#use a dummy email for testing
email_reciever = 'terey95673@notedns.com'

subject = 'Test Email'

body = 'This is a test email'

msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_reciever
msg['Subject'] = subject
msg.set_content(body)

context = ssl.create_default_context()

#Would be better to use an API now, but this is the quick and dirty way
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, msg.as_string())
    print('You did it! ...Email sent successfully')

