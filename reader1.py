# Simple SMTP mail reader
# Example

import poplib
from email import parser
import getpass

pop_conn = poplib.POP3_SSL('pop.gmail.com')

# prompt for gmail account id and password
username=raw_input('GMail Account :')
passwd=getpass.getpass('Password :')

pop_conn.user(username)
pop_conn.pass_(passwd)

# Get messages from server
print 'connecting '
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

# Concat message pieces
print 'joining message ..'
messages = ["\n".join(mssg[1]) for mssg in messages]

# Parse message intom an email object:
print 'parsing email...'
messages = [parser.Parser().parsestr(mssg) for mssg in messages]
print 'parsing done'
print messages

#
pop_conn.quit()


