# import imaplib
# import email

# imap_host = 'imap.your-email-provider.com'
# username = 'your-email@example.com'
# password = 'your-password'
# mail = imaplib.IMAP4_SSL(imap_host)
# mail.login(username, password)
# mail.select('inbox')
# status, response = mail.search(None, 'ALL')
# mail_ids = response[0].split()
# if mail_ids:
#     status, data = mail.fetch(mail_ids[0], '(RFC822)') 
#     for response_part in data:
#         if isinstance(response_part, tuple):
#             msg = email.message_from_bytes(response_part[1])
#             if msg.is_multipart():
#                 for part in msg.walk():
#                     content_type = part.get_content_type()
#                     content_disposition = part.get('Content-Disposition')
#                     if content_type == 'text/plain' and content_disposition is None:
#                         body = part.get_payload(decode=True).decode('utf-8')
#                         print(body.decode('utf-8'))
#             else:
#                 print(msg.get_payload(decode=True).decode('utf-8'))
# else:
#     print("No mails found!")

# mail.close()
# mail.logout()


# -*- encoding=utf8 -*-
__author__ = "xfdzl"

from airtest.core.api import *
import imaplib
import email
auto_setup(__file__)

imap_host = 'outlook.office365.com'
username = "Xu.Xu@versuni.com"
password = "xfdzl@489119"
mail = imaplib.IMAP4_SSL(imap_host)
mail.login(username,password)
mail.select("inbox")
status,response = mail.search(None,'ALL')
mail_ids = response[0].split()
if mail_ids:
    status,data = mail.fetch(mail_ids[0],'RFC822')
    for response_part in data:
        if isinstance(response_part,tuple):
            msg = email.message_from_bytes(response_part[1])
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = part.get('Content-Disposition')
                    if content_type == 'text/plain' and content_disposition is None:
                        body = part.get_payload(decode = True).decode('UTF-8')
                        print(body.decode('UTF-8'))
            else:
                        print(msg.get_payload(decode = True).decode('UTF-8'))
else:
    print("没有收到验证码邮件！")
mail.close()
mail.logout()





