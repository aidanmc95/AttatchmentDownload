import imaplib
import base64
import os
import email
from decouple import config

email = config('email')
email_password = config('emailpassword')

print(email, email_password)

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email, email_password)
mail.select('Inbox')

# type, data = mail.search(None, 'ALL')
# mail_ids = data[0]
# id_list = mail_ids.split()