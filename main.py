import imaplib
import base64
import os
import email
from decouple import config

# Base Info
email_user = config('email')
email_password = config('emailpassword')
subject = 'Reporting Flow'

# Get Email Info
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(email_user, email_password)
mail.select('Inbox')

# Get Ids
type, data = mail.search(None,'(SUBJECT "%s")' % subject)
mail_ids = data[0]
id_list = mail_ids.split()

# Get Email Data
typ, data = mail.fetch(id_list[0], '(RFC822)' )
raw_email = data[0][1]

raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

def getAttachment(msg,check):
    for part in msg.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/Users/aidanmuller-cohn/Development/code/AttatchmentDownload/', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]

payload = getAttachment(email_message,lambda x: x.endswith('.txt'))

if __name__ == '__main__':
    print('hi')