#!/usr/bin/python
# -*- coding: utf-8 -*-

# -----------------------------------------------
# Filename    : send_mail.py
# Discription : 
# Usage       : 
# -----------------------------------------------

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

FROM_ADDRESS = ""
TO_ADDRESS = ""

def send_mail(from_addr, to_addr, subject, text):
    charset = "ISO-2022-JP"

    msg = MIMEText(text.encode(charset), "plain", charset)
    msg["Subject"] = Header(subject,charset)
    msg["From"]    = from_addr
    msg["To"]      = to_addr
    msg["Date"]    = formatdate(localtime = True)

    smtp = smtplib.SMTP("localhost")
    smtp.sendmail(from_addr,to_addr,msg.as_string())
    smtp.close()

    return


def main():
    from_address = FROM_ADDRESS
    to_address = TO_ADDRESS
    subject = "test"
    text = "test"

    send_mail(from_address, to_address, subject, text)

    return

if __name__ == '__main__':
    main()
