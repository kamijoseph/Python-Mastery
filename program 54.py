
# Email Sender app

from email.message import EmailMessage
import ssl
import smtplib
password = None
email_sender = 'josephkiarie561gmail.com'
email_password = password

email_receiver = 'nairobibusinessboysgmail.com'

subject = "Forget to sub"
body = """

when you watch a video, please hit subscribe

"""

em = EmailMessage()
em ['From'] = email_sender
em ['To'] = email_receiver
em ['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())