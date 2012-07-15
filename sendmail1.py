# Sendmail1 - SMTP test program
#
import smtplib

 
# 
# please replace username and password with proper value before testing
to = 'toname@hotmail.com'
gmail_user = 'fromname@gmail.com'
gmail_pwd = 'thepassword'

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
