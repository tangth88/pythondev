# Sendmail1 - SMTP test program
# Date : July 15, 2012
# Objective : To develop the baseline sendmail utlity in Python
#
import smtplib
import getpass

# 
# please input username and password with proper value before testing
# Use GMail SMTP server for outgoing mail
to = raw_input('To Address:')
gmail_user = raw_input('From Address:')
gmail_pwd = raw_input('GMail Password:')

#
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

#
#
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:sendmail1.py test\n'
print header
msg = header + '\n test message sent by sendmail1.py test utl\n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'

#
smtpserver.close()
