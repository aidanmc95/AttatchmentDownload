import imaplib
import base64
import os
import email
from decouple import config

email_user = config('email')
email_password = config('emailpassword')
subject = 'Reporting Flow'

print(email, email_password)

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_user, email_password)
mail.select('Inbox')

type, data = mail.search(None,'(SUBJECT "%s")' % subject)
mail_ids = data[0]
id_list = mail_ids.split()

typ, data = mail.fetch(id_list[0], '(RFC822)' )
raw_email = data[0][1]

raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

print(raw_email_string)

if __name__ == '__main__':
    print('hi')